# coding:utf-8
"""
problem: https://leetcode.com/contest/weekly-contest-172/problems/maximum-69-number/

1323. Maximum 69 Number
User Accepted:3668
User Tried:3725
Total Accepted:3753
Total Submissions:4559
Difficulty:Easy
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



Example 1:

Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.


Constraints:

1 <= num <= 10^4
num's digits are 6 or 9

题目大意是说，通过一次6和9的变换，使得原来的数字可以达到最大。
"""


class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        result = [number for number in str_num ]
        result_len = len(result)
        for result_index in range(result_len):
            if result[result_index] == '6':
                result[result_index] = '9'
                break
        return int(''.join(res for res in result))


if __name__ == '__main__':
    num = 6699
    solution = Solution()
    result = solution.maximum69Number(num)
    print(result)
