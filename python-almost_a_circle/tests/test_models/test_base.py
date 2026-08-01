#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittests for Base.__init__ and the id counter."""

    def setUp(self):
        """Reset the private id counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_default(self):
        """Test that the id auto-increments when not given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        """Test that a given id is used as-is."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_given_does_not_affect_counter(self):
        """Test that giving an id doesn't advance the auto counter."""
        b1 = Base(12)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_id_none_explicit(self):
        """Test that explicitly passing None behaves like no id."""
        b = Base(None)
        self.assertEqual(b.id, 1)


class TestBaseToJsonString(unittest.TestCase):
    """Unittests for Base.to_json_string."""

    def test_none(self):
        """Test that None returns "[]"."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """Test that an empty list returns "[]"."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """Test a normal list of dictionaries."""
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, '[{"id": 1}]')

    def test_return_type(self):
        """Test that the return value is a string."""
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)


class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for Base.from_json_string."""

    def test_none(self):
        """Test that None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """Test that an empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        """Test a normal JSON string of a list of dicts."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(result, [{"id": 1}])

    def test_round_trip(self):
        """Test that to_json_string and from_json_string are inverses."""
        original = [{"id": 1, "width": 2}]
        json_str = Base.to_json_string(original)
        self.assertEqual(Base.from_json_string(json_str), original)


class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for Base.save_to_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_creates_file(self):
        """Test that the file is created with the class name."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_none_saves_empty_list(self):
        """Test that passing None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_content_round_trip(self):
        """Test that saved content matches the objects' dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(
            Base.from_json_string(content), [r1.to_dictionary()])

    def test_overwrites_existing_file(self):
        """Test that an existing file is overwritten, not appended."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        Rectangle.save_to_file([Rectangle(2, 2)])
        with open("Rectangle.json", "r") as f:
            content = Base.from_json_string(f.read())
        self.assertEqual(len(content), 1)


class TestBaseCreate(unittest.TestCase):
    """Unittests for Base.create."""

    def test_create_rectangle(self):
        """Test that create builds a Rectangle with the given attrs."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

    def test_create_is_new_instance(self):
        """Test that create returns a distinct object."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test that create builds a Square with the given attrs."""
        s1 = Square(5, 1, 2)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


class TestBaseLoadFromFile(unittest.TestCase):
    """Unittests for Base.load_from_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_no_file_returns_empty_list(self):
        """Test that a missing file returns an empty list."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_round_trip_rectangle(self):
        """Test saving and reloading a list of Rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(loaded[0]))
        self.assertEqual(str(r2), str(loaded[1]))

    def test_round_trip_square(self):
        """Test saving and reloading a list of Squares."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(str(s1), str(loaded[0]))
        self.assertEqual(str(s2), str(loaded[1]))

    def test_loaded_instances_are_correct_type(self):
        """Test that loaded instances are of the requesting class."""
        Square.save_to_file([Square(5)])
        loaded = Square.load_from_file()
        self.assertIsInstance(loaded[0], Square)


if __name__ == "__main__":
    unittest.main()
