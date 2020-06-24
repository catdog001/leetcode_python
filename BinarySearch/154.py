"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums or len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]

    left, right = 0, len(nums) - 1
    #
    # if nums[left] > nums[right]:
    #     return nums[left]
    # 如果全部是重复元素
    if len(set(nums)) == 1:
        return nums[0]
    while (left <= right):
        mid = int(left + (right - left) / 2)
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        # 如果区间内全部为重复元素
        if len(set(nums[left: right + 1])) == 1:
            return nums[left]
        # 右半部分不降序
        # 右半部分升序
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] == nums[right]:
            right = right - 1
        elif nums[mid] > nums[left]:
            left = mid + 1
        elif nums[mid] == nums[left]:
            left = left + 1


if __name__ == '__main__':
    nums = [2,2,2,0,1]
    min_number = findMin(nums)
    print(min_number)