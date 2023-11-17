#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
"""

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)

    # Create a new State object
    new_state = State(name="California")
    # Create a new City object
    new_city = City(name="San Francisco")
    # Link the new city to the new state
    new_state.cities.append(new_city)
    # Add the new state to the session
    session.add(new_state)
    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
