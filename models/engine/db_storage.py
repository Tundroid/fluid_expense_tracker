#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import Database
from models.budget import Budget
from models.category import Category
from models.expense import Expense
from models.income import Income
from models.saving_goal import SavingGoal
from models.saving import Saving
from models.user import User
from os import getenv
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    "budger": Budget,
    "category": Category,
    "expense": Expense,
    "income": Income,
    "saving_goal": SavingGoal,
    "saving": Saving,
    "user": User
}


class DBStorage:
    """interaacts with the MySQL database"""
    __engines = [None, None]
    __sessions = [None, None]

    def __init__(self):
        """Instantiate a DBStorage object"""
        APP_MYSQL_USER = getenv("MOLe_MYSQL_USER")
        APP_MYSQL_PWD = getenv("MOLe_MYSQL_PWD")
        APP_MYSQL_HOST = getenv("MOLe_MYSQL_HOST")
        APP_MYSQL_DB_COMMERCE = getenv("MOLe_MYSQL_MAIN_DB")
        APP_MYSQL_DB_ACCOUNT = getenv("MOLe_MYSQL_USER_ACC")
        APP_ENV = getenv("MOLe_ENV")
        self.__engines[Database.ACCOUNT.value] = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                    APP_MYSQL_USER,
                    APP_MYSQL_PWD,
                    APP_MYSQL_HOST,
                    APP_MYSQL_DB_ACCOUNT)
            )
        self.__engines[Database.COMMERCE.value] = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                    APP_MYSQL_USER,
                    APP_MYSQL_PWD,
                    APP_MYSQL_HOST,
                    APP_MYSQL_DB_COMMERCE))
        if APP_ENV == "test":
            pass

    def all(self, cls=None, db=Database.COMMERCE):
        """query on the current database session"""
        new_dict = {}
        class_dict = classes_commerce | classes_account
        if cls:
            class_dict = {key: val for key, val in class_dict.items() if val == cls}
        for my_class in class_dict.values():
            objs = self.__sessions[db.value].query(my_class).all()
            for obj in objs:
                obj_id = ("-".join([str(getattr(obj, k.name))
                                    for k in inspect(cls).primary_key]))
                key = f"{obj.__class__.__name__}.{obj_id}"
                new_dict[key] = obj
        return (new_dict)

    def new(self, obj, db=Database.COMMERCE):
        """add the object to the current database session"""
        self.__sessions[db.value].add(obj)

    def save(self, db=Database.COMMERCE):
        """commit all changes of the current database session"""
        self.__sessions[db.value].commit()

    def delete(self, obj, db=Database.COMMERCE):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__sessions[db.value].delete(obj)

    def reload(self):
        """reloads data from the database"""
        # TODO try to create all db with the following
        for i in range(2):
            sess_factory = sessionmaker(bind=self.__engines[i],
                                        expire_on_commit=False)
            self.__sessions[i] = scoped_session(sess_factory)

    def close(self):
        """call remove() method on the private session attribute"""
        for i in range(2):
            self.__sessions[i].remove()

    def get(self, cls, ids):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        db = (Database.COMMERCE if cls in classes_commerce.values()
              else Database.ACCOUNT)

        return (self.__sessions[db.value].query(cls)
                        .filter_by(**ids).first())

    def count(self, cls=None, db=Database.COMMERCE):
        """
        count the number of objects in storage
        """
        classes = classes_commerce | classes_account

        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas, db=db).values())
        else:
            count = len(models.storage.all(cls, db=db).values())

        return count

    def clean(self, cls):
        """
        clear all records in given table represented by @cls
        """
        db = models.storage.get_db(cls)
        # Disable foreign key checks
        self.__sessions[db].execute(text("SET FOREIGN_KEY_CHECKS = 0"))

        # Truncate the table
        self.__sessions[db].execute(text(f"TRUNCATE TABLE {cls.__tablename__}"))

        # Re-enable foreign key checks
        self.__sessions[db].execute(text("SET FOREIGN_KEY_CHECKS = 1"))

        self.save()

    def get_db(self, cls):
        return Database.COMMERCE.value if cls in classes_commerce.values() else Database.ACCOUNT.value
