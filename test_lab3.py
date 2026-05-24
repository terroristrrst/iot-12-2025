import unittest
from sem2_lab3 import BinaryTree, binary_tree_diameter

class TestBinaryTreeDiameter(unittest.TestCase):
    def test_single_node(self):
        root = BinaryTree(1)
        self.assertEqual(binary_tree_diameter(root), 0)

    def test_linear_tree(self):
        root = BinaryTree(1, BinaryTree(2, BinaryTree(3, BinaryTree(4))))
        self.assertEqual(binary_tree_diameter(root), 0)

    def test_full_tree(self):
        root = BinaryTree(1, BinaryTree(2, BinaryTree(4), BinaryTree(5)), BinaryTree(3, BinaryTree(6), BinaryTree(7)))
        self.assertEqual(binary_tree_diameter(root), 4)  # путь 4 -> 2 -> 1 -> 3 -> 7

if __name__ == "__main__":
    unittest.main()
