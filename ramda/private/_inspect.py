
from inspect import getfullargspec

from ._isPlaceholder import _isPlaceholder


def funcArgsLength(fn):
  """
  Get the number of args for function fn
  Not count *args and **kwargs
  """
  return fn.__code__.co_argcount


def getArgsToUse(fn, args):
  """
  Get args to use for fn
  """
  if getfullargspec(fn).varargs:
    # we can not determine the number of args if varargs exists
    return args
  argsToUse = []
  for i in range(funcArgsLength(fn)):
    if not _isPlaceholder(args[i]):
      argsToUse.append(args[i])
  return argsToUse
