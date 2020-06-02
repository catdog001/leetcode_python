# coding:utf-8
"""
problem: https://leetcode.com/contest/weekly-contest-172/problems/maximum-69-number/
unittest
"""
import unittest
from max_69_number import Solution


class Testmaximum69Number(unittest.TestCase):

    def test_maximum69Number(self):
        "test"
        solution = Solution()
        test1 = solution.maximum69Number(6699)
        self.assertEqual(test1, 9699)
        test2 = solution.maximum69Number(6666)
        self.assertEqual(test2, 9666)
        test3 = solution.maximum69Number(9999)
        self.assertEqual(test3, 9999)


