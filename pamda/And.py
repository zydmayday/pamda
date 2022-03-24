from pamda.private._curry2 import _curry2


def inner_and(a, b):
  return a and b


And = _curry2(inner_and)
"""
Because `and` is a keyword in Python, so we instead use And.
"""
