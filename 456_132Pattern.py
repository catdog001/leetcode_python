"""

"""


class Solution(object):
    def find132pattern_solution1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        超时，改进以下
        """

        if len(nums) <= 2:
            return False

        # dp[i]表示在nums中以i为结尾的中间序列是否满足条件

        dp = [0 for _ in range(len(nums))]

        for num_index in range(0, len(nums)):
            for less_than_num_index in range(num_index):
                for greater_than_num_index in range(num_index,len(nums),1):
                    if nums[greater_than_num_index] > nums[less_than_num_index] \
                            and nums[greater_than_num_index] < nums[num_index]:
                        dp[num_index] = 1
                        break
        return True if sum(dp) > 0 else False

    def find132pattern_solution2(self, nums):
