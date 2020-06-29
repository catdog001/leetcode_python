"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
该题采用257同样的思路，然后判断和值是否存在于所有路径的和的列表中来判断
"""


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 采用深度搜索-前序遍历看下
        if not root:
            return False
        allPaths = []

        def getAllPaths(root, single_path):
            if not root:
                return
            single_path += int(root.val)
            if not root.left and not root.right:
                allPaths.append(single_path)
            else:
                getAllPaths(root.left, single_path)
                getAllPaths(root.right, single_path)
        single_path = 0
        getAllPaths(root, single_path)
        return True if sum in allPaths else False