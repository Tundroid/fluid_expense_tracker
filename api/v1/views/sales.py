#!/usr/bin/python3
""" Sales API endpoints """


# Standard library imports
import importlib
import re
import requests

# Third-party imports
from flask import request, abort, jsonify, url_for
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError, Schema, fields
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
import logging


# Local imports
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import classes_commerce, classes_account
from .creators import create_model

logging.basicConfig(level=logging.DEBUG)  # Set log level
logger = logging.getLogger(__name__)

class SaleSchema(Schema):
    """
    Sale schema.

    This schema defines the structure of the Sales data.

    Attributes:
        details (Dict): Record details.
        records (List): List of record(s).
    """
    details = fields.Dict(required=True, doc="Record details")
    records = fields.List(fields.Dict(), required=True, doc="List of record(s)")


@app_views.route("/sell", methods=['POST'], strict_slashes=False)
@jwt_required()
def create_sale():
    """
    Create a new model instance.

    Args:
        request body: JSON data for the new model instance.

    Returns:
        JSON response with the created model data or an error message.

    Errors:
        400: Invalid request (e.g., missing model or invalid JSON)
        404: Model not found
        409: Resource already exists
    """

    try:
        request_data = request.get_json(silent=True)
        if not request_data:
            raise BadRequest()

        classes = classes_commerce | classes_account
        model = "record_detail"
        db_model = classes[model]

        schema = SaleSchema(many=True) if type(request_data) is list else SaleSchema()

        # Validate the data
        request_data = schema.load(request_data)

        data_set = [request_data] if type(request_data) is dict else request_data
        headers = { "Authorization": request.headers.get('Authorization') }
        for data in data_set:
            response = requests.post("http://localhost:5000/api/v1/create/record_detail",
                                     json=data["details"], headers=headers)
            if response.status_code == 201:
                response = requests.post("http://localhost:5000/api/v1/create/record",
                                         json=data["records"], headers=headers)
                if response.status_code != 201:
                    return response.text, response.status_code
            else:
                return response.text, response.status_code
            # obj = db_model(**data)
            # storage.new(obj)
        # storage.save()
        return '', 201
    except KeyError:
        abort(404, description={"message": f"Model `{model}`"})
    except IntegrityError as e:
        match = re.search(r"Duplicate entry '(.+?)'", str(e.orig))
        duplicate_value = match.group(1) if match else "Unknown"
        abort(409, description={"message": f"Resource(s) already exists in Model `{model}`, check value(s) `{duplicate_value}`"})
    except ValidationError as e:
        msg = {"message": f"Error(s) found in data for Model `{model}`, see details"}
        msg["detail"] = e.messages
        abort(400, description=msg)
    except BadRequest:
        abort(400, description={"message": "Valid JSON data required"})
