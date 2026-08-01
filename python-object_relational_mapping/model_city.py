#!/usr/bin/python3
"""Contains the class definition of a City."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Represents a city in the MySQL database."""

    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
    state = relationship("State")
