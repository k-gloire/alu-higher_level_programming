#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareInit(unittest.TestCase):
    """Unittests for Square.__init__."""

    def setUp(self):
        """Reset the private id counter before each test."""
        Base._Base__nb_objects = 0

    def test_width_equals_height(self):
        """Test that width and height are both set to size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_x_y_id_assigned(self):
        """Test that x, y, and id are assigned correctly."""
        s = Square(3, 1, 3, 12)
        self.assertEqual((s.x, s.y, s.id), (1, 3, 12))

    def test_is_rectangle_instance(self):
        """Test that a Square is also a Rectangle instance."""
        self.assertIsInstance(Square(5), Rectangle)

    def test_no_extra_attributes(self):
        """Test that Square does not define new instance attributes."""
        s = Square(5)
        expected_attrs = {
            "_Rectangle__width", "_Rectangle__height",
            "_Rectangle__x", "_Rectangle__y", "id",
        }
        self.assertEqual(set(s.__dict__.keys()), expected_attrs)


class TestSquareValidation(unittest.TestCase):
    """Unittests confirming Square inherits Rectangle's validation."""

    def test_size_not_int(self):
        """Test that a non-int size raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_negative(self):
        """Test that a negative size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_size_zero(self):
        """Test that a zero size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_negative(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)


class TestSquareArea(unittest.TestCase):
    """Unittests for Square.area (inherited from Rectangle)."""

    def test_area(self):
        """Test the area of a square."""
        self.assertEqual(Square(5).area(), 25)

    def test_area_size_one(self):
        """Test the area of a size-1 square."""
        self.assertEqual(Square(1).area(), 1)


class TestSquareStr(unittest.TestCase):
    """Unittests for Square.__str__."""

    def test_str_format(self):
        """Test the exact __str__ output format."""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_offset(self):
        """Test __str__ with non-zero x/y offsets."""
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")


class TestSquareSize(unittest.TestCase):
    """Unittests for the Square size property."""

    def test_size_getter(self):
        """Test that size returns the current width."""
        self.assertEqual(Square(5).size, 5)

    def test_size_setter_updates_both(self):
        """Test that setting size updates width and height together."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_validation(self):
        """Test that the size setter validates like width does."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_negative(self):
        """Test that a negative size raises ValueError."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for Square.update with *args."""

    def test_update_id_only(self):
        """Test updating only the id via args."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_all_args(self):
        """Test updating every attribute via args, in order."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    def test_update_partial_args(self):
        """Test updating only id and size via args."""
        s = Square(5)
        s.update(1, 2)
        self.assertEqual((s.id, s.size), (1, 2))
        self.assertEqual((s.x, s.y), (0, 0))


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for Square.update with **kwargs."""

    def test_update_single_kwarg(self):
        """Test updating a single attribute via kwargs."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(s.x, 12)

    def test_update_multiple_kwargs(self):
        """Test updating several attributes via kwargs at once."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual((s.id, s.size, s.y), (89, 7, 1))

    def test_kwargs_ignored_when_args_present(self):
        """Test that kwargs are skipped entirely if args is non-empty."""
        s = Square(5, id=1)
        s.update(1, size=99)
        self.assertEqual(s.size, 5)


class TestSquareToDictionary(unittest.TestCase):
    """Unittests for Square.to_dictionary."""

    def test_dictionary_keys_and_values(self):
        """Test that the dictionary has the correct keys and values."""
        s = Square(10, 2, 1, 5)
        expected = {"id": 5, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_round_trip_via_update(self):
        """Test that applying to_dictionary via update recreates state."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
