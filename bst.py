import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BinTree : TypeAlias = Union[None, 'BSNode']
@dataclass(frozen=True)
class BSNode:
    val: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any],bool]
    other: BinTree
    def is_empty(self)-> bool:
        if self.other is None:
            return True
        else:
            return False

    def insert(self, t : 'BinarySearchTree', val: Any)-> 'BinarySearchTree':
        def insert_helper(t: BinTree, val: Any):
            match t:
                case None:
                    return BSNode(val, None, None)
                case BSNode(v, l, r):
                    if self.comes_before(t.val,v):
                        return BSNode(t.val, insert_helper(l, val), r)
                    else :
                        return BSNode(v, l, insert_helper(r, val))
# Not done








def example_fun(x : int) -> bool:
    return x < 142
