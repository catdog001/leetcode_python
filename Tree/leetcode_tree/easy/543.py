"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

 

注意：两结点之间的路径长度是以它们之间边的数目表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题意理解，该题是任意两个节点的路径最大值看成是树的直径。
注意是任意两点！
测试样例：[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]。
两结点之间的路径长度是以它们之间边的数目表示。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 直径应该是左子树的高度+右子树的高度的最大值
        def get_height(root):
            if not root:
                return 0
            left = get_height(root.left)
            right = get_height(root.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return max(left, right) + 1

        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        get_height(root)
        return self.max_diameter

