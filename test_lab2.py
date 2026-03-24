import unittest
from sem2_lab2 import max_min_distance

class TestAggressiveCows(unittest.TestCase):

    def test_example(self):
        N = 5
        C = 3
        free_sections = [1, 2, 8, 4, 9]
        self.assertEqual(max_min_distance(N, C, free_sections), 3)


if __name__ == "__main__":
    unittest.main()