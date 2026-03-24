class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _insert(self, node, value, priority):
        if not node:
            return Node(value, priority)

        if priority > node.priority:
            node.left = self._insert(node.left, value, priority)
        else:
            node.right = self._insert(node.right, value, priority)

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        return node

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def _find_max(self, node):
        while node.left:
            node = node.left
        return node

    def _delete_max(self, node):
        if node.left is None:
            return node.right, node
        node.left, max_node = self._delete_max(node.left)
        return node, max_node

    def pop_max(self):
        if not self.root:
            return None
        self.root, max_node = self._delete_max(self.root)
        return (max_node.value, max_node.priority)

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append((node.value, node.priority))
        self._inorder(node.right, result)

    def view_queue(self):
        result = []
        self._inorder(self.root, result)
        return result