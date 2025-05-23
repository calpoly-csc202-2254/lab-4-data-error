import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10 ** 6)

BinTree: TypeAlias = Union[None, 'BSNode']


@dataclass(frozen=True)
class BSNode:
    val: Any
    left: BinTree
    right: BinTree


@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    other: BinTree

    def is_empty(self) -> bool:
        return self.other is None

    def insert(self, t: 'BinarySearchTree', val: Any) -> 'BinarySearchTree':
        tree = insert_helper(t.other, val, self.comes_before)
        return BinarySearchTree(self.comes_before, tree)

    def lookup(self, t: 'BinarySearchTree', val: Any) -> bool:
        return lookup_helper(t.other, val, self.comes_before)

    def delete(self, t: 'BinarySearchTree', val1: Any) -> BinTree:
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
                        return BSNode(v, l, delete_helper(r))

        return delete_helper(t.other)


def insert_helper(t: BinTree, val: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
    match t:
        case None:
            return BSNode(val, None, None)
        case BSNode(v, l, r):
            if comes_before(val, v):
                return BSNode(v, insert_helper(l, val, comes_before), r)
            else:
                return BSNode(v, l, insert_helper(r, val, comes_before))


def lookup_helper(t: BinTree, val: Any, comes_before: Callable[[Any, Any], bool])-> bool:
    match t:
        case None:
            return False
        case BSNode(v, l, r):
            if comes_before(v, val) is False and comes_before(val, v) is False:
                return True
            elif comes_before(val, v):
                return lookup_helper(l, val, comes_before)
            else:
                return lookup_helper(r, val, comes_before)


def example_fun(x: int) -> bool:
    return x < 142
