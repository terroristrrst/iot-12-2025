import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lab9 import Trie, build_trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = build_trie(["cat", "car", "care", "dog"])

    def test_search_existing(self):
        self.assertTrue(self.trie.search("cat"))

    def test_search_non_existing(self):
        self.assertFalse(self.trie.search("cow"))

    def test_starts_with_true(self):
        self.assertTrue(self.trie.starts_with("ca"))

    def test_starts_with_false(self):
        self.assertFalse(self.trie.starts_with("xy"))

    def test_insert_new(self):
        self.trie.insert("cow")
        self.assertTrue(self.trie.search("cow"))

    def test_empty_word(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))

    def test_single_letter(self):
        self.trie.insert("a")
        self.assertTrue(self.trie.search("a"))


if __name__ == "__main__":
    unittest.main()