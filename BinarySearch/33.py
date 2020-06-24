class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True
            if nums[mid] > nums[0]:
                if target >= nums[0] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[0]:
                if target >= nums[mid] and target <= nums[len(nums)-1]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] == nums[0]:
                return True
        return False


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    solution = Solution()
    result = solution.search(nums, target)
    print(result)