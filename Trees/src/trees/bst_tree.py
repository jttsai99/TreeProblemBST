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

    def _get_height(self,node) -> int:
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

    def _get_length(self,node) -> int :
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
                        node.parent = cur
                        cur.left = node
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if (cur.right is None):
                        node.parent = cur
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
        if cur is None:
            raise MissingValueError
        return cur

    def get_max_node(self,node = None) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        if node is None:
            cur = self.root
        else:
            cur = node
        while (cur.right is not None):
            cur = cur.right
            #print(cur.value)
        return cur

    def get_min_node(self, node = None) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        if node is None:
            cur = self.root
        else:
            cur = node
        while (cur.left is not None):
            cur = cur.left
        return cur

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
        node_to_remove = self.get_node(value)  # finds the node if not found raise MissingValueError
        # print("node to remove:", node_to_remove.value)
        # print("number of children:",node_to_remove.num_children())
        if node_to_remove.has_no_children():  # check if given node have a left or right
            if node_to_remove.parent is None:  # if this is the root of the tree
                self.root = None        #set root back to none
            else:
                node_to_remove.parent.remove_child(node_to_remove)  #if it has a parent just remove itself


        elif node_to_remove.num_children() == 1:
            node_to_remove_child = node_to_remove.left if node_to_remove.left is not None else node_to_remove.right
            if node_to_remove.parent is None:       #Trying to remove root of tree No Parent
               self.root = node_to_remove_child
               self.root.parent = None
            else:       #if it is not the root and has only one child
                node_to_remove.parent.replace_child(node_to_remove,node_to_remove_child)

        else: #Two Children cases
            successor = self.get_max_node(node_to_remove.left)
            self.remove_value(self.key(successor.value))
            node_to_remove.value = successor.value
        self._num_nodes -= 1


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
