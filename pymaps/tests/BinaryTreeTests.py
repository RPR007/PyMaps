import unittest

from pymaps.trees.BinarySearchTree import BinarySearchTree


class BinaryTreeTest(unittest.TestCase):

    def test_create_tree(self):
        bt = BinarySearchTree()
        self.assertEqual(len(bt), 0)
