import unittest
from avl_priority_queue import AVLPriorityQueue

class TestAVLPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = AVLPriorityQueue()

    def test_insert_and_view(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 2)
        self.pq.insert("C", 8)
        self.pq.insert("D", 3)

        queue = self.pq.view_queue()
        expected = [("C", 8), ("A", 5), ("D", 3), ("B", 2)]
        self.assertEqual(queue, expected)

    def test_pop_max(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 2)
        self.pq.insert("C", 8)

        max_item = self.pq.pop_max()
        self.assertEqual(max_item, ("C", 8))

        max_item2 = self.pq.pop_max()
        self.assertEqual(max_item2, ("A", 5))

        max_item3 = self.pq.pop_max()
        self.assertEqual(max_item3, ("B", 2))

        self.assertIsNone(self.pq.pop_max())

    def test_empty_queue(self):
        self.assertEqual(self.pq.view_queue(), [])
        self.assertIsNone(self.pq.pop_max())

if __name__ == "__main__":
    unittest.main()