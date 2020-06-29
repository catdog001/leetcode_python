"""
二叉树的层次遍历
青岛大学 王卓老师的video：https://www.bilibili.com/video/BV1ub411A7hb
"""
"""
树的遍历，前序、中序和后序
"""
# 前序


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Level(object):

    def __init__(self):
        self.result = []

    def get_level(self, tree):
        """
        tree, iteration to complete
        :param tree:
        :return:
        """
        if tree is None:
            return None
        queue = []
        queue.append(tree)
        while len(queue) > 0:
            # queue里面是队列，故而先进先出，append是后进，pop()是指pop出append里面的元素即后入先出，pop(0)表示先入先出为队列
            # 出队为队首元素
            root = queue.pop(0)
            self.result.append(root.val)
            # stack里面是栈，故而先压入右子树，再压入左子树
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return self.result

    def create_tree(self):
        # A、L、B、E、 C、D、W、X
        A = TreeNode("A")
        L = TreeNode("L")
        B = TreeNode("B")
        E = TreeNode("E")
        C = TreeNode("C")
        D = TreeNode("D")
        W = TreeNode("W")
        X = TreeNode("X")
        A.left = L
        A.right = C
        L.left = B
        L.right = E
        C.right = D
        D.left = W
        W.right = X
        return A


if __name__ == '__main__':
    tree_level = Level()
    tree = tree_level.create_tree()
    level_result = tree_level.get_level(tree)
    # 'A', 'L', 'C', 'B', 'E', 'D', 'W', 'X'
    print("层次遍历结果是：{}".format(level_result))