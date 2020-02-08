"""
problem: https://leetcode.com/problems/print-words-vertically/
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.



Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically.
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed.
"TBONTB"
"OEROOE"
"   T"
Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]


Constraints:

1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.

题目大意：
多个字符串垂直对齐输出，其中，最大长度的左边字符串长度不足的用空格填充，右边不需要。
"""


class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_list = s.split(" ")
        results = []
        max_len = max(len(ss) for ss in s_list)
        for max_len_index in range(max_len):
            word = ""
            for element in s_list:
                if max_len_index+1 <= len(element):
                    word = word + element[max_len_index]
                else:
                    word = word + " "
            word = word.rstrip()
            results.append(word)
        return results


if __name__ == '__main__':
    s = "TO BE OR NOT TO BE"
    solution = Solution()
    results = solution.printVertically(s)
    print(results)


