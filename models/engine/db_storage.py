#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


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

    def all(self, cls=None):
        """uery on the current database session (self.__session)
        all objects depending of the class name"""
        if cls is None:
            classes = [State, City, User, Place, Review, Amenity]
            objects = []
            for classe in classes:
                objects.extend(self.__session.query(classe).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objects = self.__session.query(cls).all()
        
        result = {}
        for obj in objects:
            result["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
        return result