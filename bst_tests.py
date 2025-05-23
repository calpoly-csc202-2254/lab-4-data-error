import sys
import unittest
from typing import *
from dataclasses import dataclass
import math

import bst

sys.setrecursionlimit(10 ** 6)

from bst import *


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def comes_before_num(a: int, b: int):
    return a < b


def comes_before_abc(a: str, b: str):
    return a < b


def comes_before_euclidean(a: Point, b: Point):
    dist_a = ((a.x ** 2) + (a.y ** 2)) ** 0.5
    dist_b = ((b.x ** 2) + (b.y ** 2)) ** 0.5
    return dist_a < dist_b


bt1 = BSNode(8, BSNode(3, None, None), BSNode(10, None, None))
bt2 = BSNode("E", BSNode("D", None, None), BSNode("G", None, None))

bst1 = BinarySearchTree(comes_before_num, bt1)
bst2 = BinarySearchTree(comes_before_abc, bt2)
bst3 = BinarySearchTree(comes_before_num, None)


class BSTTests(unittest.TestCase):
    def test_is_empty(self):
        self.assertEqual(True, bst3.is_empty())
        self.assertEqual(False, bst1.is_empty())

    def test_insert_helper(self):
        expected = BSNode(8, BSNode(3, BSNode(2, None, None), None), BSNode(10, None, None))
        expected2 = BSNode("E", BSNode("D", BSNode("A", None, None), None), BSNode("G", None, None))
        self.assertEqual(expected, insert_helper(bt1, 2, comes_before_num))
        self.assertEqual(expected2, insert_helper(bt2, "A", comes_before_abc))
        # needs euclidean test case

    def test_insert(self):
        pass

    def test_look_up_helper(self):
        self.assertEqual(False, lookup_helper(bt1, 2, comes_before_num))
        self.assertEqual(True, lookup_helper(bt2, "E", comes_before_abc))
      #   needs euclidean test case

def test_example_fun(self):
    self.assertEqual(True, example_fun(34))
    self.assertEqual(False, example_fun(1423))


if (__name__ == '__main__'):
    unittest.main()
