"""
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-univalue-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
https://blog.csdn.net/qq_27806947/article/details/100568990
最长同值路径只会来源于三个方面：
1、只存在于左子树
2、只存在于右子树
3、同时存在于左右子树，并穿过节点
注意：如果当前节点与左节点的值不同，那么左边的同值路径就会断掉（路径值清零，从0开始）。
同理，如果和右节点值不同，右边的同值路径就会断掉（（路径值清零，从0开始）。
以某个节点为根节点的最长同值路径就是，
如果该节点的值等于其左子树的值，则最长同值路径要加上左子树的最长同值路径，如果不等，左子树的路径为0
如果该节点的值等于其右子树的值，则最长同值路径要加上右子树的最长同值路径，如果不等，右子树的路径为0
"""

