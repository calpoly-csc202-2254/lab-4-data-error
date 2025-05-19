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
    comes_before: Callable[[], ]
    other: BinTree
comes_before(self, a: BinTree):
        if self.val < a.val:
            return True


def example_fun(x : int) -> bool:
    return x < 142
