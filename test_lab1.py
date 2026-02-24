import unittest
from sem2_lab1 import find_kth_largest


class TestKthLargest(unittest.TestCase):

    def test_normal_case(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        value, index = find_kth_largest(arr, 3)
        self.assertEqual(value, 22)
        self.assertEqual(index, 2)

    def test_k_equals_1(self):
        arr = [3, 1, 5, 2]
        value, index = find_kth_largest(arr, 1)
        self.assertEqual(value, 5)
        self.assertEqual(index, 2)

    def test_k_equals_len(self):
        arr = [3, 1, 5, 2]
        value, index = find_kth_largest(arr, 4)
        self.assertEqual(value, 1)
        self.assertEqual(index, 1)

    def test_single_element(self):
        arr = [10]
        value, index = find_kth_largest(arr, 1)
        self.assertEqual(value, 10)
        self.assertEqual(index, 0)

    def test_invalid_k(self):
        arr = [1, 2, 3]
        with self.assertRaises(ValueError):
            find_kth_largest(arr, 5)


if __name__ == '__main__':
    unittest.main()