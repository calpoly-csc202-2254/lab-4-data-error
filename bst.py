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

    def lookup(self, t: 'BinarySearchTree', val: Any) -> bool:
        def lookup_helper(t: BinTree):
            match t:
                case None:
                    return False
                case BSNode(v, l , r):
                    if self.comes_before(v, val) is False and self.comes_before(val, v) is False:
                        return True
                    elif self.comes_before(val, v):
                        return lookup_helper(l)
                    else:
                        return lookup_helper(r)
        return lookup_helper(t.other)

    def delete(self, t:'BinarySearchTree', val1: Any) -> BinTree:
        def val_check(val, com_val):
            return self.comes_before(val, com_val) is False and self.comes_before(com_val, val) is False

        def left_min(t: BinTree):
            match t:
                case BSNode(v, None, r):
                    return v
                case BSNode(v, l, r):
                    return left_min(l)

        def delete_helper(t: BinTree):
            match t:
                case None:
                    return None
                case BSNode(v, None, None):
                    if val_check(v, val1):
                        return None
                    else:
                        return t
                case BSNode(v, None, r):
                    if val_check(v, val1):
                        return r
                    else:
                        return BSNode(v, None, delete_helper(r))
                case BSNode(v, l, None):
                    if val_check(v, val1):
                        return l
                    else:
                        return BSNode(v, delete_helper(l), None)
                case BSNode(v, l, r):
                    if val_check(v, val1):
                        return BSNode(left_min(r), l, delete_helper(r))
                    elif self.comes_before(val1, v):
                        return BSNode(v, delete_helper(l), r)
                    else:
                        return BSNode(v,l,delete_helper(r))

        return delete_helper(t.other)









def example_fun(x : int) -> bool:
    return x < 142
