"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
解题思路：
对于二叉树来说，就看三个部分：根、左子树、右子树。具体左子树和右子树可能还有子树，这个先不管，用递归来处理。
对于该题来说，给定两棵树，t1和t2。即对于t1和t2，分别有t1的根、左子树、右子树三个部分和t2的根、左子树、右子树。
两树合并边界条件有2个：
- t1和t2都是空，那么返回空（t1和t2返回都行）
- t1或者t2为空，返回t1 or t2就好（即返回不为空的那个）
当两棵树都不为空时，递归合成新树（递归的方法记为mergeTwoTrees）。递归的边界条件即为上述两个，
代码也分成三个部分：
- 新树的根，root = TreeNode(t1.val + t2.val)，即为两个根值的和作为根
- 新树的左孩子， 即为两棵树的左孩子做merge，root.left = mergeTwoTrees(t1.left, t2.left)
- 新树的右孩子， 即为两棵树的右孩子做merge，root.right = mergeTwoTrees(t1.right, t2.right)
返回新树的根就好。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 or not t2:
            return t1 or t2
        if not t1 and not t2:
            return t1

        def mergeTwoTrees(t1, t2):
            if not t1 or not t2:
                return t1 or t2
            if not t1 and not t2:
                return t1
            if t1 or t2:
                root = TreeNode(t1.val + t2.val)
                root.left = mergeTwoTrees(t1.left, t2.left)
                root.right = mergeTwoTrees(t1.right, t2.right)
                return root

        new_root = mergeTwoTrees(t1, t2)
        return new_root