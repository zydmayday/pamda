from .private._curry2 import _curry2
from .private._helper import toNumber

subtract = _curry2(lambda a, b: toNumber(a) - toNumber(b))
