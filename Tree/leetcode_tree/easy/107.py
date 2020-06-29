"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
解题思路：当遍历树的根节点时，按(节点, 节点序号)压栈，根节点为(根节点, 0)，然后其左右孩子为其父节点的序号加1压栈。最后按节点序号进行排序，同一个节点序号的合并
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []

        # 存入结果为[(节点值, 层次编号)]，同一个层次编号的元素放在同一个列表中
        single_result = []
        if not root:
            return []
        # 队列元素中加入层次序号
        queue = []
        # 根节点为0号
        queue.append((root, 0))

        while len(queue) > 0:
            # 注意队列，故而为pop(0)。如果是栈，为pop()
            node = queue.pop(0)

            # 当开始为空的时候，表明列表中需要加入新列表，列表元素为[(node[0].val, node[1])]，因为node形式是（节点，层次编号）
            if len(single_result) == 0:
                single_result.append([(node[0].val, node[1])])
            else:
                # 如果该node的层次编号和single_result最新放入的元素编号相同，将新元素列表扩充，single_result形式为[[(节点值，节点编号)]]
                if node[1] == single_result[-1][-1][1]:
                    single_result[-1] += [(node[0].val, node[1])]
                else:
                    single_result.append([(node[0].val, node[1])])

            # 如果存在左孩子，层次编号node[1]加1
            if node[0].left:
                queue.append((node[0].left, node[1] + 1))
            # 如果存在右孩子，层次编号node[1]加1。如果同一个节点的左右孩子，层次编号一样
            if node[0].right:
                queue.append((node[0].right, node[1] + 1))
        # [[(3, 0)], [(9, 1), (20, 1)], [(15, 2), (7, 2)]]
        # print(single_result)
        for ele in single_result:
            result = []
            for single_ele in ele:
                result.append(single_ele[0])
            results.append(result)
        return results[::-1]