#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import BaseModel, Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
                    pool_pre_ping=True
        )

        # drop all tables if the environment variable HBNB_ENV is equal to test
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)
        
        # Create tables if they don't exist
        Base.metadata.created_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
