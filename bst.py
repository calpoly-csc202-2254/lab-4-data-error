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


def example_fun(x : int) -> bool:
    return x < 142
