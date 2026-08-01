# Python - Almost a circle

This project is part of the ALU Higher Level Programming curriculum. It
covers classes, inheritance, private attributes with getters/setters,
class/static methods, `*args`/`**kwargs`, unit testing, and
serialization/deserialization with JSON.

## Structure

```
models/
    __init__.py
    base.py        # Base class: id management, JSON, file persistence
    rectangle.py    # Rectangle class, inherits from Base
    square.py       # Square class, inherits from Rectangle
tests/
    __init__.py
    test_models/
        __init__.py
        test_base.py
        test_rectangle.py
        test_square.py
```

## Running the tests

```
python3 -m unittest discover tests
```

Or file by file:

```
python3 -m unittest tests/test_models/test_base.py
python3 -m unittest tests/test_models/test_rectangle.py
python3 -m unittest tests/test_models/test_square.py
```

## Author

Jessica
