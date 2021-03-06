import unittest

from Trees.src.errors import MissingValueError
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode


class TestBST(unittest.TestCase):
    def test_create_empty_tree(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)

    def test_create_tree(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)


    def test_tree_not_eq(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(92)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertNotEqual(tree, cmp_tree)

    def test_get_max_node(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(90)
        tree.add_value(200)
        tree.add_value(70)

        self.assertEqual(BSTNode(200),tree.get_max_node())

    def test_get_max_node2(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(90)
        tree.add_value(200)
        tree.add_value(70)
        node_to_remove = tree.get_node(80)
        self.assertEqual(BSTNode(90),tree.get_max_node(node_to_remove))

    def test_get_min_node(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(90)
        tree.add_value(200)
        tree.add_value(70)

        self.assertEqual(BSTNode(70),tree.get_min_node())

    def test_get_node(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(90)
        tree.add_value(200)
        tree.add_value(70)
        self.assertEqual(BSTNode(70), tree.get_node(70))

    def test_get_node_error(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(90)
        tree.add_value(200)
        tree.add_value(70)
        self.assertRaises(MissingValueError, tree.get_node, 50)


    def test_remove_value(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(90)
        tree.add_value(200)
        tree.add_value(70)
        tree.remove_value(80)
        #tree.print_tree()

    #.left.right stuff that butner did in his test cases for other tree
        othertree = BST()
        othertree.add_value(100)
        othertree.add_value(70)
        othertree.add_value(200)
        othertree.add_value(90)
        #othertree.print_tree()
        self.assertEqual(tree, othertree)

    def test_remove_value_len(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(90)
        tree.add_value(200)
        tree.add_value(70)
        #print(len(tree))
        tree.remove_value(80)
        #print(len(tree))
        #tree.print_tree()
        self.assertEqual(4, len(tree))

    def test_remove_root_nochildren(self):
        tree=BST()
        tree.add_value(100)
        #print("tree length:",len(tree))
        tree.remove_value(100)
        #print("tree length after:",len(tree))
        self.assertEqual(0, len(tree))

    def test_remove_root_one_children(self):
        tree=BST()
        tree.add_value(100)
        tree.add_value(50)
        print("tree length:",len(tree))
        tree.remove_value(100)
        print("tree length after:",len(tree))
        self.assertEqual(1, len(tree))

if __name__ == '__main__':
    unittest.main()
