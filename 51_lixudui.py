class Solution:
    def reversePairs(self, nums):
        count = 0
        nums_len = len(nums)
        if not nums or nums_len < 2:
            return 0
        if nums_len == 2:
            if nums[0] > nums[1]:
                return 1
            else:
                return 0
        for index in range(nums_len):
            count += sum(list([1 if nums[index] > nums[index_j] else 0 for index_j in range(index+1, nums_len)]))
        return count

if __name__ == "__main__":
    solution = Solution()
    result = solution.reversePairs([5,4,3,2,1])
    print(result)
