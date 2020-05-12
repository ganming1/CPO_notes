import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *


class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(cons('a', None)), 1)
        self.assertEqual(size(cons('a', cons('b', None))), 2)

    def test_cons(self):
        self.assertEqual(cons('a', None), Node('a', None))
        self.assertEqual(cons('a', cons('b', None)), Node('a', Node('b', None)))

    def test_remove(self):
        self.assertRaises(AssertionError, lambda: remove(None, 'a'))
        self.assertRaises(AssertionError, lambda: remove(cons('a', None), 'b'))
        self.assertEqual(remove(cons('a', cons('a', None)), 'a'), cons('a', None))
        self.assertEqual(remove(cons('a', cons('b', None)), 'a'), cons('b', None))
        self.assertEqual(remove(cons('a', cons('b', None)), 'b'), cons('a', None))

if __name__ == '__main__':
    unittest.main()
