import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from lab6_tribes import count_pairs


class TestTribes(unittest.TestCase):

    def test_example1(self):
        pairs = [(1, 2), (2, 4), (3, 5)]
        self.assertEqual(count_pairs(pairs), 4)

    def test_example2(self):
        pairs = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        self.assertEqual(count_pairs(pairs), 6)

    def test_single_tribe(self):
        pairs = [(1, 2)]
        self.assertEqual(count_pairs(pairs), 0)

    def test_two_tribes_no_common(self):
        pairs = [(1, 3), (2, 4)]
        self.assertEqual(count_pairs(pairs), 4)

    def test_mixed_tribes(self):
        pairs = [(1, 2), (1, 3), (3, 4), (5, 6)]
        self.assertEqual(count_pairs(pairs), 4)

    def test_empty_input(self):
        pairs = []
        self.assertEqual(count_pairs(pairs), 0)

    def test_large_numbers(self):
        pairs = [(1001, 2002), (2002, 3001), (4002, 5001)]
        self.assertEqual(count_pairs(pairs), 3)


if __name__ == "__main__":
    unittest.main()