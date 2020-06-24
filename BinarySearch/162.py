"""

"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        nums[i]\nums[i+1]构成一个排序数组，即每两个元素构成一个排序数组，不足两个（1个数组元素一定是有序的），归并排序的思路，等价于求解最大值就好
        """
        if not nums or len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            elif nums[0] < nums[1]:
                return nums[1]
            # 这个条件不可能成立，题目中要求nums[i]\nums[i+1]不想等
            elif nums[0] == nums[1]:
                return None
        left, right = 0, len(nums) - 1
        max_number = nums[0]
        max_number_index = 0
        while left <= right:
            if right == left + 1:
                if max_number < nums[right]:
                    max_number = nums[right]
                    max_number_index = right
                return max_number_index

            if nums[left] > nums[left + 1]:
                if max_number < nums[left]:
                    max_number = nums[left]
                    max_number_index = left
            elif nums[left] < nums[left + 1]:
                if max_number < nums[left + 1]:
                    max_number = nums[left + 1]
                    max_number_index = left + 1

            left = left + 2

        return max_number_index


if __name__ == '__main__':
    nums = [1,2,1,3,5,6,4]
    solution = Solution()
    max_number_index = solution.findPeakElement(nums)
    print(max_number_index)