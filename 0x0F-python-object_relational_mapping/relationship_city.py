#!/usr/bin/python3
"""
This module contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """
    City class
    - inherits from Base
    - links to the MySQL table cities
    - class attribute id representing a column of an auto-generated,
    unique integer, can't be null and is a primary key
    - class attribute name representing a column of a string with
    maximum 128 characters and can't be null
    - class attribute state_id representing a column of an integer,
    can't be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement="auto"
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
