"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
非递归方法进行中序遍历，因为递归可以用栈来进行模拟，故而需要借助于数据结构栈。
左右孩子节点需要以根节点为基础，在知道根节点的情况下才可以访问左右孩子节点。故而当访问根节点时需要将根节点入栈保存。同时将左孩子节点赋值给根节点（记为p）
直到某一个根节点的左孩子为空，此时将栈中元素出栈（此时出栈的为根节点元素）即为q，然后将该节点的右孩子节点赋值给根节点（p = q.right)。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # 中序遍历结果
        result = []
        # 栈
        stack = []
        while root or len(stack) > 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                result.append(tmp.val)
                root = tmp.right
        return result
