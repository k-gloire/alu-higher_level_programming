#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for the max_integer function."""

    def test_ordered_list(self):
        """Test a list already in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list in no particular order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test a list in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_start(self):
        """Test the maximum being the first element."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Test the maximum being the last element."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test that calling with no argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-5, -1, -10, -3]), -1)

    def test_mixed_positive_negative(self):
        """Test a list mixing positive and negative numbers."""
        self.assertEqual(max_integer([-5, 3, -10, 7, 0]), 7)

    def test_all_same_values(self):
        """Test a list where every element is identical."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_duplicate_max(self):
        """Test a list where the max value appears more than once."""
        self.assertEqual(max_integer([3, 9, 9, 2]), 9)


if __name__ == "__main__":
    unittest.main()
