import unittest
from test.helpers.listXf import listXf

import pamda as R

"""
https://github.com/ramda/ramda/blob/master/test/any.js
"""


def odd(n): return n % 2 == 1
def T(): return True
# TODO: intoArray


class TestAny(unittest.TestCase):
  def test_returns_true_if_any_elements_satisfy_the_predicate(self):
    self.assertEqual(True, R.any(odd, [2, 4, 6, 8, 10, 11, 12]))

  def test_returns_false_if_all_elements_fails_to_satisfy_the_predicate(self):
    self.assertEqual(False, R.any(odd, [2, 4, 6, 8, 10, 12]))

  # TODO: intoArray

  def test_works_with_more_complex_objects(self):
    people = [{'first': 'Paul', 'last': 'Grenier'}, {'first': 'Mike', 'last': 'Hurley'}, {'first': 'Will', 'last': 'Klein'}]
    def alliterative(person): return person.get('first')[0] == person.get('last')[0]
    self.assertEqual(False, R.any(alliterative, people))
    people.append({'first': 'Scott', 'last': 'Sauyet'})
    self.assertEqual(True, R.any(alliterative, people))

  def test_returns_false_for_an_empty_list(self):
    self.assertEqual(False, R.any(T, []))

  def test_dispatches_when_given_a_transformer_in_list_position(self):
    res = R.any(odd, listXf)
    self.assertEqual(res.any, False)
    self.assertEqual(res.f, odd)
    self.assertEqual(res.xf, listXf)


if __name__ == '__main__':
  unittest.main()
