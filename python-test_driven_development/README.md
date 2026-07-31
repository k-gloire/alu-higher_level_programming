# Python - Test-driven development

This project is part of the ALU Higher Level Programming curriculum. It
covers test-driven development in Python: writing doctest-based
interactive tests and unittest-based unit tests before/alongside the
functions they verify.

## Files

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds two numbers, casting floats to int first |
| `2-matrix_divided.py` | Returns a new matrix with every element divided by a number |
| `3-say_my_name.py` | Prints "My name is `<first>` `<last>`" |
| `4-print_square.py` | Prints a square of `#` characters |
| `5-text_indentation.py` | Prints text with blank lines after `.`, `?`, and `:` |
| `6-max_integer.py` | Returns the maximum integer in a list |
| `tests/0-add_integer.txt` | Doctest suite for `0-add_integer.py` |
| `tests/2-matrix_divided.txt` | Doctest suite for `2-matrix_divided.py` |
| `tests/3-say_my_name.txt` | Doctest suite for `3-say_my_name.py` |
| `tests/4-print_square.txt` | Doctest suite for `4-print_square.py` |
| `tests/5-text_indentation.txt` | Doctest suite for `5-text_indentation.py` |
| `tests/6-max_integer_test.py` | Unittest suite for `6-max_integer.py` |

## Running the tests
python3 -m doctest ./tests/*
python3 -m unittest tests.6-max_integer_test
