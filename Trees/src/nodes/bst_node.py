import copy
from typing import Generic, Iterable, TypeVar, Optional

from Trees.src.errors import MissingValueError

T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: gert the right child
    """
    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        self.value = value  # donor object or int or whatever type

        if children == None:
            self.left = None
            self.right = None
        else:
            self.left = next(children)
            self.right = next(children)

        self.parent = parent


    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    def __deepcopy__(self, memodict) -> "BSTNode[T]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        copy_node = BSTNode(copy.deepcopy(self.value, memodict))
        copy_node.left = copy.deepcopy(self.left, memodict)
        copy_node.right = copy.deepcopy(self.right, memodict)
        return copy_node


    def num_children(self) -> int:
        if self.left is not None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1
        elif self.left is not None and self.right is not None:
            return 2
        else:
            return 0

    def has_no_children(self) -> bool:
        return self.num_children() == 0

    def remove_child(self,node):
        self.replace_child(node,None)

    def replace_child(self,targetnode,replacementnode):
        if targetnode is self.left:
            self.left = replacementnode
        else:
            self.right = replacementnode
        if replacementnode is not None:
            replacementnode.parent = self
        if targetnode is not None:
            targetnode.parent = None



    def __eq__(self, other: Optional['BSTNode[T]']) -> bool:
        raise NotImplementedError()
        # if isinstance(other,BSTNode):
        #     return self.value == other.value
        # else:
        #     return False