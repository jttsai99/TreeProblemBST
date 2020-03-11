import copy
from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')


class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
        """
        You must have at least one member named root

        :param root: The root node of the tree if there is one.
        If you are provided a root node don't forget to count how many nodes are in it
        :param key: The function to be applied to a node's value for comparison purposes.
        It serves the same role as the key function in the min, max, and sorted builtin
        functions
        """
        self.root = root
        self.key = key  # created the function already and automatically grabs the amount from the object
        self._num_nodes = 1
        # self.add_value(value)
        ...

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        return self._get_height(self.root)

    def _get_height(self,node):
        if node is None:
            return -1
        left_side = self._get_height(node.left)
        right_side = self._get_height(node.right)

        return 1 + max(left_side, right_side)

    def __len__(self) -> int:
        """
        :return: the number of nodes in the tree
        """
        return self._get_length(self.root)

    def _get_length(self,node):
        if node is None:
            return 0
        else:
            left_side = self._get_length(node.left)
            right_side = self._get_length(node.right)
            return left_side + right_side + 1

    def add_value(self, value: T) -> None:
        """
        Add value to this BST
        Duplicate values should be placed on the right
        :param value:
        :return:
        """
        node = BSTNode(value)
        if (self.root is None):
            self.root = node
            node.left = None
            node.right = None
        else:
            cur = self.root
            while (cur is not None):
                if (self.key(node.value) < self.key(cur.value)):
                    if (cur.left is None):
                        cur.left = node
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if (cur.right is None):
                        cur.right = node
                        cur = None
                    else:
                        cur = cur.right
            node.left = None
            node.right = None

        self._num_nodes += 1

    def get_node(self, value: K) -> BSTNode[T]:
        """
        Get the node with the specified value
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        cur = self.root
        while (cur is not None):
            if (value == self.key(cur.value)):
                return cur
            elif (value < self.key(cur.value)):
                cur = cur.left
            else:
                cur = cur.right
            return None

    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        cur = self.root
        while (cur.right is not None):
            cur = cur.right
        return cur.value

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        cur = self.root
        while (cur.left is not None):
            cur = cur.left
        return cur.value

    def remove_value(self, value: K) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
        ...

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       BST(self.root.left) == BST(other.root.left) and \
                       BST(self.root.right) == BST(other.root.right)
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    def __deepcopy__(self, memodict) -> "BST[T,K]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        new_root = copy.deepcopy(self.root, memodict)
        new_key = copy.deepcopy(self.key, memodict)
        return BST(new_root, new_key)
