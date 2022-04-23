# python_ramda

This is a repo try to copy <https://github.com/ramda/ramda> in python.

## install

For whom wants to use this package.

```bash
> pip install python_ramda
> pip install python_ramda -U # get the latest
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
# see: https://pre-commit.com/ for more details
$ pre-commit install # please install hooks first
```

Checkout new branch from `main` branch directly and create PR.

## CheckList

Functions supported now.

- [x] __
- [x] add

```python
  # different from ramda, ramda treat null as 0
  >>> R.add(None, None) # float('nan)
```

- [ ] addIndex
- [x] adjust
- [x] all
  - Transducer part is not fully tested.
- [ ] allPass
- [x] always
- [x] And (`and` is a keyword in python)
- [ ] andThen
- [x] any
- [ ] anyPass
- [ ] ap
- [ ] aperture
- [x] append
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
- [x] clone

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
- [x] comparator
- [ ] complement
- [x] compose
- [ ] composeWith
- [x] concat
- [ ] cond
- [ ] construct
- [ ] constructN
- [ ] converge
- [ ] count
- [x] countBy
- [x] curry
- [x] curryN
- [ ] dec
- [ ] defaultTo
- [ ] descend
- [x] difference
- [x] differenceWith
- [ ] dissoc
- [ ] dissocPath
- [x] divide
- [x] drop
- [ ] dropLast
- [ ] dropLastWhile
- [ ] dropRepeats
- [ ] dropRepeatsWith
- [ ] dropWhile
- [ ] either
- [ ] empty
- [ ] endsWith
- [ ] eqBy
- [x] eqProps

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

- [x] equals
- [ ] evolve
- [x] F
- [x] filter
- [x] find
- [ ] findIndex
- [ ] findLast
- [ ] findLastIndex
- [x] flatten
- [x] flip
- [ ] forEach
- [ ] forEachObjIndexed
- [ ] fromPairs
- [x] groupBy
- [ ] groupWith
- [ ] gt
- [ ] gte
- [ ] has
- [ ] hasIn
- [ ] hasPath
- [ ] head
- [ ] identical
- [x] identity
- [ ] ifElse
- [ ] inc
- [ ] includes
- [ ] indexBy
- [ ] indexOf
- [ ] init
- [ ] innerJoin
- [ ] insert
- [ ] insertAll
- [ ] intersection
- [ ] intersperse
- [x] into
- [ ] invert
- [ ] invertObj
- [ ] invoker
- [ ] is
- [ ] isEmpty
- [ ] isNil
- [ ] join
- [ ] juxt
- [x] keys

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
- [ ] lastIndexOf
- [ ] length
- [ ] lens
- [ ] lensIndex
- [ ] lensPath
- [ ] lensProp
- [ ] lift
- [ ] liftN
- [ ] lt
- [ ] lte
- [x] Map (`map` is a keyword in python)
- [ ] mapAccum
- [ ] mapAccumRight
- [ ] mapObjIndexed
- [ ] match
- [ ] mathMod
- [ ] max
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
- [ ] min
- [ ] minBy
- [ ] modify
- [ ] modifyPath
- [ ] modulo
- [ ] move
- [x] multiply
- [ ] nAry
- [ ] negate
- [ ] none
- [ ] not
- [x] nth
- [ ] nthArg
- [ ] o
- [x] objOf
- [ ] of
- [ ] omit
- [ ] on
- [ ] once
- [ ] or
- [ ] otherwise
- [ ] over
- [ ] pair
- [ ] partial
- [ ] partialObject
- [ ] partialRight
- [ ] partition
- [ ] path
- [ ] pathEq
- [ ] pathOr
- [ ] paths
- [ ] pathSatisfies
- [ ] pick
- [ ] pickAll
- [ ] pickBy
- [x] pipe
- [ ] pipeWith
- [ ] pluck
- [ ] prepend
- [ ] product
- [ ] project
- [ ] promap
- [x] prop
- [ ] propEq
- [ ] propIs
- [ ] propOr
- [ ] props
- [ ] propSatisfies
- [x] range
- [x] reduce
- [x] reduceBy
- [x] reduced
- [ ] reduceRight
- [ ] reduceWhile
- [x] reject
- [ ] remove
- [ ] repeat
- [ ] replace
- [x] reverse
- [ ] scan
- [ ] sequence
- [ ] set
- [x] slice
- [x] sort
- [ ] sortBy
- [ ] sortWith
- [ ] split
- [ ] splitAt
- [ ] splitEvery
- [ ] splitWhen
- [ ] splitWhenever
- [ ] startsWith
- [ ] subtract
- [ ] sum
- [ ] symmetricDifference
- [ ] symmetricDifferenceWith
- [x] T
- [x] tail
- [ ] take
- [ ] takeLast
- [ ] takeLastWhile
- [ ] takeWhile
- [ ] tap
- [ ] test
- [ ] thunkify
- [ ] times
- [ ] toLower
- [ ] toPairs
- [ ] toPairsIn
- [ ] toString
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
- [ ] union
- [ ] unionWith
- [ ] uniq
- [ ] uniqBy
- [ ] uniqWith
- [ ] unless
- [ ] unnest
- [ ] until
- [ ] unwind
- [ ] update
- [ ] useWith
- [ ] values
- [ ] valuesIn
- [ ] view
- [ ] when
- [ ] where
- [ ] whereAny
- [ ] whereEq
- [ ] without
- [ ] xor
- [ ] xprod
- [ ] zip
- [ ] zipObj
- [ ] zipWith
