#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from os import getenv
from models.review import Review
from models.amenity import Amenity
from models import storage
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
            primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
            primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")


    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """
            get the list of Amenities linked to place
            """
            my_amenities = []
            all_instan_amenities = list(storage.all(Amenity).values())
            for amenity in all_instan_amenities:
                if amenity.id in self.amenity_ids:
                    my_amenities.append(amenity)
            return my_amenities

        @amenities.setter
        def amenities(self, value):
            """set amenities that handles append method for adding
            an Amenity.id to the attribute amenity_ids
            """
            if isinstance(value, "Amenity"):
                self.amenity_ids.append(value.id)
