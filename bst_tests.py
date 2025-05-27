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
bt3 = BSNode(6,
             BSNode(5, None, None),
             BSNode(10,
                    BSNode(7,
                           None,
                           BSNode(9,
                                  BSNode(8,None, None),
                                  None)),
                    BSNode(11, None, None)))
bt4 = BSNode(6,
             None,
             BSNode(10,
                    BSNode(7,
                           None,
                           BSNode(9,
                                  BSNode(8,None, None),
                                  None)),
                    BSNode(11, None, None)))
bt5 = BSNode("d",
             BSNode("c",
                    BSNode("b",
                           BSNode("a", None,None),
                           None),
                    None),
             BSNode("k",
                    BSNode("j",
                           None,
                           BSNode("h",
                                  BSNode("g",None, None),
                                  None)),
                    BSNode("z", None, None)))
bt6 = BSNode(Point(3,3), BSNode(Point(2,4), None, None), BSNode(Point(5,6), None, None))
bt7 = BSNode(Point(10,8), BSNode(Point(3,4), BSNode(Point(2,2),None, None) ,None), BSNode(Point(22,5), None, None))

bst1 = BinarySearchTree(comes_before_num, bt1)
bst2 = BinarySearchTree(comes_before_abc, bt2)
bst3 = BinarySearchTree(comes_before_num, None)
bst4 = BinarySearchTree(comes_before_euclidean, bt7)
bst5 = BinarySearchTree(comes_before_num,bt3)
bst6 = BinarySearchTree(comes_before_abc,bt5)


class BSTTests(unittest.TestCase):
    def test_is_empty(self):
        self.assertEqual(True, bst3.is_empty())
        self.assertEqual(False, bst1.is_empty())

    def test_insert_helper(self):
        expected = BSNode(8, BSNode(3, BSNode(2, None, None), None), BSNode(10, None, None))
        expected2 = BSNode("E", BSNode("D", BSNode("A", None, None), None), BSNode("G", None, None))
        expected3 = BSNode(Point(3,3), BSNode(Point(2,4), BSNode(Point(1,1),None, None), None), BSNode(Point(5,6), None, None))
        self.assertEqual(expected, insert_helper(bt1, 2, comes_before_num))
        self.assertEqual(expected2, insert_helper(bt2, "A", comes_before_abc))
        self.assertEqual(expected3, insert_helper(bt6, Point(1,1), comes_before_euclidean))


    def test_insert(self):
        change1= BSNode(Point(10,8), BSNode(Point(3,4), BSNode(Point(2,2), None, None) ,None), BSNode(Point(22,5), BSNode(Point(15,9),None, None),None))
        change2 = BSNode(8, BSNode(3, BSNode(0,None,None), None), BSNode(10, None, None))
        change3 = BSNode("E", BSNode("D",BSNode("C", None, None), None,), BSNode("G", None, None))
        expected = BinarySearchTree(comes_before_euclidean, change1)
        expected2 = BinarySearchTree(comes_before_num, change2)
        expected3 = BinarySearchTree(comes_before_abc, change3)
        self.assertEqual(expected,bst4.insert(Point(15,9)))
        self.assertEqual(expected2,bst1.insert(0))
        self.assertEqual(expected3,bst2.insert("C"))


    def test_look_up_helper(self):
        self.assertEqual(False, lookup_helper(bt1, 2, comes_before_num))
        self.assertEqual(True, lookup_helper(bt2, "E", comes_before_abc))
        self.assertEqual(True, lookup_helper(bt6, Point(5,6), comes_before_euclidean))
        self.assertEqual(False, lookup_helper(bt6, Point(0,6), comes_before_euclidean))

    def test_lookup(self):
        self.assertEqual(True, bst1.lookup(10))
        self.assertEqual(False, bst1.lookup(5))
        self.assertEqual(True, bst2.lookup("E"))
        self.assertEqual(False, bst2.lookup("z"))
        self.assertEqual(True, bst4.lookup(Point(3,4)))
        self.assertEqual(False, bst4.lookup(Point(9,3)))

    def test_value_check(self):
        self.assertEqual(True, val_check(2,2, comes_before_num))
        self.assertEqual(True, val_check("e", "e", comes_before_abc))
        self.assertEqual(False, val_check(3, 6, comes_before_num))
        self.assertEqual(True, val_check(Point(4,4), Point(4,4), comes_before_euclidean))
        self.assertEqual(False, val_check("hello", "hi", comes_before_abc))

    def test_left_min(self):
        self.assertEqual(5, left_min(bt3))
        self.assertEqual(6,left_min(bt4))
        self.assertEqual("a", left_min(bt5))

    def test_delete_helper(self):
        self.assertEqual(BSNode(6,
                                BSNode(5, None, None),
                                BSNode(10,
                                        BSNode(9,
                                                BSNode(8,None, None),
                                                None),
                                        BSNode(11, None, None))), delete_helper(bt3, 7, comes_before_num))
        self.assertEqual(BSNode(6,
                                BSNode(5, None, None),
                                BSNode(11,
                                       BSNode(7,
                                       None,
                                       BSNode(9,
                                              BSNode(8,None, None),
                                              None)),
                                       None)), delete_helper(bt3,10,comes_before_num))
        self.assertEqual(BSNode(Point(10,8),
                                BSNode(Point(2,2),None, None),
                                BSNode(Point(22,5), None, None)), delete_helper(bt7, Point(3,4), comes_before_euclidean))
        self.assertEqual( BSNode("d",
                                 BSNode("c",
                                        BSNode("a", None,None),
                                 None),
                                BSNode("k",
                                       BSNode("j",
                                              None,
                                              BSNode("h",
                                                     BSNode("g",None, None),
                                       None)),
                                BSNode("z", None, None))), delete_helper(bt5, "b", comes_before_abc))

    def test_delete(self):
        self.assertEqual(BSNode(6,
                                BSNode(5, None, None),
                                BSNode(10,
                                        BSNode(9,
                                                BSNode(8,None, None),
                                                None),
                                        BSNode(11, None, None))), bst5.delete(7))
        self.assertEqual(BSNode("d",
                                 BSNode("c",
                                        BSNode("a", None,None),
                                 None),
                                BSNode("k",
                                       BSNode("j",
                                              None,
                                              BSNode("h",
                                                     BSNode("g",None, None),
                                       None)),
                                BSNode("z", None, None))), bst6.delete("b"))
        self.assertEqual(BSNode(Point(10,8),
                                BSNode(Point(2,2),None, None),
                                BSNode(Point(22,5), None, None)), bst4.delete(Point(3,4)))



def test_example_fun(self):
    self.assertEqual(True, example_fun(34))
    self.assertEqual(False, example_fun(1423))


if (__name__ == '__main__'):
    unittest.main()
