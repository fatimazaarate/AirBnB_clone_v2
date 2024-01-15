#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
<<<<<<< HEAD
    places= relationship("Place", backref="user", cascade="delete")
    reviews= relationship("Review", backref="user", cascade="delete")
=======
    places = relationship("Place", backref="user", cascade="delete")
>>>>>>> 7ed89a156bb59c766ed000f73ecf2381b1eeb71c
