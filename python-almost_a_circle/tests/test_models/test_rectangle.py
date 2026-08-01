#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
import unittest
import unittest.mock
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInit(unittest.TestCase):
    """Unittests for Rectangle.__init__."""

    def setUp(self):
        """Reset the private id counter before each test."""
        Base._Base__nb_objects = 0

    def test_basic_attributes(self):
        """Test that width, height, x, y are assigned correctly."""
        r = Rectangle(10, 2, 1, 9, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 9)
        self.assertEqual(r.id, 12)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id_auto_assigned(self):
        """Test that id is auto-assigned when not given."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_is_base_instance(self):
        """Test that a Rectangle is also a Base instance."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)


class TestRectangleValidation(unittest.TestCase):
    """Unittests for the Rectangle attribute setters/validation."""

    def test_width_not_int(self):
        """Test that a non-int width raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_not_int(self):
        """Test that a non-int height raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_width_negative(self):
        """Test that a negative width raises ValueError."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_width_zero(self):
        """Test that a zero width raises ValueError."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = 0

    def test_height_negative(self):
        """Test that a negative height raises ValueError."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -1

    def test_x_not_int(self):
        """Test that a non-int x raises TypeError."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}

    def test_x_negative(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_y_not_int(self):
        """Test that a non-int y raises TypeError."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = "0"

    def test_y_negative(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_x_zero_is_valid(self):
        """Test that x = 0 is accepted (boundary case)."""
        r = Rectangle(10, 2, 0)
        self.assertEqual(r.x, 0)

    def test_width_bool_rejected(self):
        """Test that a bool width is rejected as not a true integer."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)

    def test_x_string(self):
        """Test that a string x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_y_string(self):
        """Test that a string y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_height_zero(self):
        """Test that a zero height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangleArea(unittest.TestCase):
    """Unittests for Rectangle.area."""

    def test_area_basic(self):
        """Test area for a simple rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_square_shape(self):
        """Test area when width equals height."""
        self.assertEqual(Rectangle(5, 5).area(), 25)

    def test_area_large(self):
        """Test area for larger dimensions."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)


class TestRectangleDisplay(unittest.TestCase):
    """Unittests for Rectangle.display."""

    def test_display_no_offset(self):
        """Test display output with no x/y offset."""
        r = Rectangle(2, 2)
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake:
            r.display()
            self.assertEqual(fake.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        """Test display output respects x and y offsets."""
        r = Rectangle(2, 1, 1, 1)
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake:
            r.display()
            self.assertEqual(fake.getvalue(), "\n ##\n")


class TestRectangleStr(unittest.TestCase):
    """Unittests for Rectangle.__str__."""

    def test_str_format(self):
        """Test the exact __str__ output format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_offsets(self):
        """Test __str__ with default x/y."""
        r = Rectangle(5, 5, id=1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 5/5")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unittests for Rectangle.update with *args."""

    def test_update_id_only(self):
        """Test updating only the id via args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_all_args(self):
        """Test updating every attribute via args, in order."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 2, 3, 4, 5))

    def test_update_partial_args(self):
        """Test updating only the first few attributes via args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual((r.id, r.width, r.height), (89, 2, 3))
        self.assertEqual((r.x, r.y), (10, 10))

    def test_update_no_args_no_kwargs(self):
        """Test that calling update with nothing changes nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unittests for Rectangle.update with **kwargs."""

    def test_update_single_kwarg(self):
        """Test updating a single attribute via kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_multiple_kwargs(self):
        """Test updating several attributes via kwargs at once."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(
            (r.id, r.width, r.x, r.y), (89, 2, 3, 1))

    def test_kwargs_ignored_when_args_present(self):
        """Test that kwargs are skipped entirely if args is non-empty."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(1, height=99)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.height, 10)


class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for Rectangle.to_dictionary."""

    def test_dictionary_keys_and_values(self):
        """Test that the dictionary has the correct keys and values."""
        r = Rectangle(10, 2, 1, 9, 3)
        expected = {"id": 3, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_dictionary_type(self):
        """Test that the return value is a dict."""
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_round_trip_via_update(self):
        """Test that applying to_dictionary via update recreates state."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
