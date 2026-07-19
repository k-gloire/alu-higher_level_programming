# Python - Everything is object

This project explores Python's object model at a low level: what `id()`
and `type()` reveal about an object, the difference between mutable
objects (list, dict, set, bytearray) and immutable objects (int, float,
str, tuple, frozenset, bytes), how variable assignment works through
references rather than copying, and how Python passes arguments to
functions by object reference. It also covers CPython's small-integer
caching (NSMALLPOSINTS/NSMALLNEGINTS) and the special case of tuples and
frozensets containing mutable objects.
