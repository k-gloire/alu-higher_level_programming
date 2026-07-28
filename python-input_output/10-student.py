#!/usr/bin/python3
"""Module that defines a Student class with a filterable JSON export."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: the student's first name.
            last_name: the student's last name.
            age: the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student instance.

        Args:
            attrs: an optional list of attribute names to include.
                If it is not a list, every attribute is included.

        Returns:
            A dictionary of the requested attributes and their values.
        """
        if isinstance(attrs, list) and all(
                isinstance(a, str) for a in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__
