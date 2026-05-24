import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from wchain import max_chain_length

class TestWordChain(unittest.TestCase):
    def test_example_1(self):
        words = [
            "crates", "car", "cats", "crate", "rate",
            "at", "ate", "tea", "rat", "a"
        ]
        self.assertEqual(max_chain_length(words), 6)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(max_chain_length(words), 4)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        self.assertEqual(max_chain_length(words), 1)

    def test_single_word(self):
        self.assertEqual(max_chain_length(["a"]), 1)

    def test_empty_list(self):
        self.assertEqual(max_chain_length([]), 0)

    def test_chain_of_four(self):
        words = ["abcd", "abc", "ab", "a", "acd"]
        self.assertEqual(max_chain_length(words), 4)

    def test_duplicates(self):
        words = ["a", "ab", "ab", "abc"]
        self.assertEqual(max_chain_length(words), 3)

if __name__ == '__main__':
    unittest.main()