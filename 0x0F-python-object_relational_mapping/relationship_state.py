#!/usr/bin/python3
"""
This module contains the class definition of a State.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    State class
    - inherits from Base
    - links to the MySQL table states
    - class attribute id representing a column of an auto-generated,
    unique integer, can't be null and is a primary key
    - class attribute name representing a column of a string with
    maximum 128 characters and can't be null
    - class attribute cities representing a relationship with the City class
    """
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement="auto"
            )
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
