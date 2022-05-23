# python_ramda

This is a repo try to copy <https://github.com/ramda/ramda> in python.

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

## install

For whom wants to use this package.

```bash
> pip install python-ramda
> pip install python-ramda -U # get the latest
```

## Usage

```python
>>> from ramda import curry
>>> def sum(a, b, c): return a + b + c
>>> curry(sum)(1)(2, 3)
6
```

```python
>>> import ramda as R # similar to ramda syntax
>>> def sum(a, b, c): return a + b + c
>>> R.curry(sum)(1)(2, 3)
6
```

## Doc

Because the usage of `python_ramda` is almostly same to `ramda`,
so we don't create any extra doc.

If you feel any behaviour is different from what is should be in `ramda`,
please check below `CheckList` for more details.

## Contribute

For whom wants to contribute to this repo.

```bash
$ pip install -U pylint
# see: https://pre-commit.com/ for more details
$ pre-commit install # please install hooks first
```

Checkout new branch from `main` branch directly and create PR.

## CheckList

Functions supported now.

- [x] 0.1.0 \_\_
- [x] 0.1.0 add

```python
# different from ramda
R.add(None, None) # float('nan)
R.add(date(1,2,3), date(1,2,3)) # float('nan)
```

- [ ] addIndex
- [x] 0.1.0 adjust
- [x] 0.1.0 all
  - Transducer part is not fully tested.
- [ ] allPass
- [x] 0.1.0 always
- [x] 0.1.0 And (`and` is a keyword in python)
- [ ] andThen
- [x] 0.1.0 any
- [ ] anyPass
- [ ] ap
- [ ] aperture
- [x] 0.1.0 append
- [ ] apply
- [ ] applySpec
- [ ] applyTo
- [ ] ascend
- [ ] assoc
- [ ] assocPath
- [ ] binary
- [ ] bind
- [ ] both
- [ ] call
- [ ] chain
- [ ] clamp
- [x] 0.1.0 clone

**we are simply using python `copy` module**
So with no specific reason, we suggest you to use python origin `copy` module as your first choice.

```python
class Obj:
  def __init__(self, x):
    self.value = x
obj = Obj(42)
clone = R.clone(obj)
obj == clone # False, obj and clone have different references
isinstance(clone, Obj) # True

class Obj:
  def __init__(self, x):
    self.value = x

  def __eq__(self, other):
    return self.value == other.value
obj = Obj(42)
clone = R.clone(obj)
obj == clone # True, if Obj override __eq__ function
isinstance(clone, Obj) # True
```

- [ ] collectBy
- [x] 0.1.0 comparator
- [ ] complement
- [x] 0.1.0 compose
- [ ] composeWith
- [x] 0.1.0 concat
- [ ] cond
- [ ] construct
- [ ] constructN
- [ ] converge
- [ ] count
- [x] 0.1.0 countBy
- [x] 0.1.0 curry
- [x] 0.1.0 curryN
- [ ] dec
- [ ] defaultTo
- [ ] descend
- [x] 0.1.0 difference
- [x] 0.1.0 differenceWith
- [ ] dissoc
- [ ] dissocPath
- [x] 0.1.0 divide
- [x] 0.1.0 drop
- [ ] dropLast
- [ ] dropLastWhile
- [ ] dropRepeats
- [ ] dropRepeatsWith
- [ ] dropWhile
- [ ] either
- [x] 0.1.0 empty

```python
# We don't support empty object in python
class Obj:
  def __init__(self, value):
    self.value = value
o = Obj(42)
o == R.empty(o) # True, we will return the original cloned object
```

What we support for now:

1. dict()
2. set()
3. list()
4. str()
5. any instance with empty() method
6. any instance with 'fantasy-land/empty' property

- [ ] endsWith
- [ ] eqBy
- [x] 0.1.0 eqProps

```python
# works for both dict and object
class Obj:
  def __init__(self, v):
    self.v = v
obj1 = Obj(1)
obj2 = Obj(1)
R.eqProps('v', obj1, obj2) # True
R.eqProps('v', {'v': 1}, {'v': 1}) # True
```

- [x] 0.1.0 equals

```python
R.equals(float('nan'), float('nan')) # True
```

- [ ] evolve
- [x] 0.1.0 F
- [x] 0.1.0 filter
- [x] 0.1.0 find
- [ ] findIndex
- [ ] findLast
- [ ] findLastIndex
- [x] 0.1.0 flatten
- [x] 0.1.0 flip
- [ ] forEach
- [ ] forEachObjIndexed
- [ ] fromPairs
- [x] 0.1.0 groupBy
- [ ] groupWith
- [x] 0.1.0 gt
- [x] 0.1.0 gte
- [ ] has
- [ ] hasIn
- [ ] hasPath
- [x] 0.1.0 head
- [ ] identical
- [x] 0.1.0 identity
- [ ] ifElse
- [ ] inc
- [ ] includes
- [ ] indexBy
- [x] 0.1.0 indexOf
- [ ] init
- [ ] innerJoin
- [ ] insert
- [ ] insertAll
- [x] 0.1.0 intersection
- [ ] intersperse
- [x] 0.1.0 into
- [ ] invert
- [ ] invertObj
- [x] 0.1.0 invoker
- [ ] is
- [x] 0.1.0 isEmpty

```python
class Obj:
  pass
# Any custom object will be treated as non-empty
R.isEmpty(Obj()) # False
R.isEmpty(None) # False
```

- [ ] isNil
- [x] 0.1.0 join
- [ ] juxt
- [x] 0.1.0 keys

```python
# When using R.keys(obj) and obj is a class instance, we use obj.__dict__ as keys.
class A:
  c = 'not included'
  def __init__(self):
    self.a = 1
    self.b = 2
a = A()
R.keys(a) # ['a', 'b']
```

- [ ] keysIn
- [ ] last
- [x] 0.1.0 lastIndexOf
- [ ] length
- [ ] lens
- [ ] lensIndex
- [ ] lensPath
- [ ] lensProp
- [ ] lift
- [ ] liftN
- [x] 0.1.0 lt
- [x] 0.1.0 lte
- [x] 0.1.0 map
- [ ] mapAccum
- [ ] mapAccumRight
- [ ] mapObjIndexed
- [x] 0.1.0 match
- [ ] mathMod
- [x] 0.1.0 Max (`max` is a keyword in python)

If R.Max(a, b)
`a` and `b` are with different types,
we will compare with str(a) and str(b).

```python
R.Max('A', None) # None, 'A' < 'None'
```

- [ ] maxBy
- [ ] mean
- [ ] median
- [ ] memoizeWith
- [ ] mergeAll
- [ ] mergeDeepLeft
- [ ] mergeDeepRight
- [ ] mergeDeepWith
- [ ] mergeDeepWithKey
- [ ] mergeLeft
- [ ] mergeRight
- [ ] mergeWith
- [ ] mergeWithKey
- [x] 0.1.0 Min (`min` is a keyword in python)

If R.Min(a, b)
`a` and `b` are with different types,
we will compare with str(a) and str(b).

```python
R.Min('A', None) # 'A', 'A' < 'None'
```

- [ ] minBy
- [ ] modify
- [ ] modifyPath
- [ ] modulo
- [ ] move
- [x] 0.1.0 multiply
- [ ] nAry
- [ ] negate
- [ ] none
- [x] 0.1.0 not
- [x] 0.1.0 nth
- [ ] nthArg
- [ ] o
- [x] 0.1.0 objOf
- [ ] of
- [x] 0.1.0 omit

we support both `dict` type and `object` type.

```python
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj = Obj(1, 2)
R.omit(['v1'], obj) # {'v2': 2}
R.omit(['v1', 'v3'], obj) # {'v2': 2}
```

- [ ] on
- [x] 0.1.0 once
- [x] 0.1.0 or
- [ ] otherwise
- [ ] over
- [ ] pair
- [ ] partial
- [ ] partialObject
- [ ] partialRight
- [ ] partition
- [x] 0.1.0 path
- [ ] pathEq
- [ ] pathOr
- [x] 0.1.0 paths
- [ ] pathSatisfies
- [x] 0.1.0 pick
- [x] 0.1.0 pickAll

both `pick` and `pickAll` support both `dict` and `object` type.

```python
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj = Obj(1, 2)
R.pick(['v1'], obj) # {'v1': 1}
R.pickAll(['v1', 'v3'], obj) # {'v1': 1, 'v3': None}
```

- [ ] pickBy
- [x] 0.1.0 pipe
- [ ] pipeWith
- [x] 0.1.0 pluck

```python
# works for both dict and object
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj1 = Obj(1, 2)
obj2 = Obj(3, 4)
R.pluck('v1', [obj1, obj2]) # [1, 3]
```

- [x] 0.1.0 prepend
- [x] 0.1.0 product
- [x] 0.1.0 project

```python
# works for both dict and object
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj1 = Obj(1, 2)
obj2 = Obj(3, 4)
R.project(['v1'], [obj1, obj2]) # [{'v1': 1}, {'v1': 3}]
```

- [ ] promap
- [x] 0.1.0 prop
- [x] 0.1.0 propEq

```python
# works for both dict and object
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj1 = Obj(1, 2)
R.propEq(1, 'v1', obj1) # True
R.propEq(2, 'v2', obj1) # True
R.propEq(1, 'v2', obj1) # False

R.propEq(1, 'v1', {'v1': 1}) # True
```

- [ ] propIs
- [ ] propOr
- [x] 0.1.0 props
- [ ] propSatisfies
- [x] 0.1.0 range
- [x] 0.1.0 reduce
- [x] 0.1.0 reduceBy
- [x] 0.1.0 reduced
- [x] 0.1.0 reduceRight
- [ ] reduceWhile
- [x] 0.1.0 reject
- [ ] remove
- [ ] repeat
- [ ] replace
- [x] 0.1.0 reverse
- [ ] scan
- [ ] sequence
- [ ] set
- [x] 0.1.0 slice

```python
R.slice(1, 3, ['a', 'b', 'c', 'd']) # ['b', 'c']
R.slice(1, None, ['a', 'b', 'c', 'd']) # ['b', 'c', 'd']
```

- [x] 0.1.0 sort
- [x] 0.1.0 sortBy
- [ ] sortWith
- [x] 0.1.0 split
- [ ] splitAt
- [ ] splitEvery
- [ ] splitWhen
- [ ] splitWhenever
- [ ] startsWith
- [x] 0.1.0 subtract

```python
# different from ramda
R.subtract(None, None) # float('nan)
R.subtract(date(1,2,3), date(1,2,3)) # float('nan)
```

- [x] 0.1.0 sum
- [ ] symmetricDifference
- [ ] symmetricDifferenceWith
- [x] 0.1.0 T
- [x] 0.1.0 tail
- [x] 0.1.0 take
- [ ] takeLast
- [ ] takeLastWhile
- [x] 0.1.0 takeWhile
- [x] 0.1.0 tap
- [ ] test
- [ ] thunkify
- [ ] times
- [ ] toLower
- [ ] toPairs
- [ ] toPairsIn
- [x] 0.1.0 toString

Partially supported

1. String type, supported
1. for others, just use str(x) instead

- [ ] toUpper
- [ ] transduce
- [ ] transpose
- [ ] traverse
- [ ] trim
- [ ] tryCatch
- [ ] type
- [ ] unapply
- [ ] unary
- [ ] uncurryN
- [ ] unfold
- [x] 0.1.0 union
- [x] 0.1.0 unionWith
- [x] 0.1.0 uniq
- [x] 0.1.0 uniqBy
- [x] 0.1.0 uniqWith
- [ ] unless
- [ ] unnest
- [ ] until
- [ ] unwind
- [ ] update
- [x] 0.1.0 useWith
- [x] 0.1.0 values

```python
# works for both dict and object
class Obj:
  def __init__(self, v1, v2):
    self.v1 = v1
    self.v2 = v2
obj = Obj(1, 2)
R.values(obj) # [1, 2]
R.values({'a': 1, 'b': 2}) # [1, 2]
```

- [ ] valuesIn
- [ ] view
- [ ] when
- [ ] where
- [ ] whereAny
- [ ] whereEq
- [ ] without
- [ ] xor
- [x] 0.1.0 xprod
- [x] 0.1.0 zip
- [ ] zipObj
- [x] 0.1.0 zipWith
