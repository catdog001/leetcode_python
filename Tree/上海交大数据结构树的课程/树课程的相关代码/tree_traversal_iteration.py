"""
树的遍历，前序、中序和后序
"""
# 前序


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Traversal(object):

    def __init__(self):
        self.result = []

    def get_preorder(self, tree):
        """
        tree, iteration to complete
        :param tree:
        :return:
        """
        if tree is None:
            return None
        stack = []
        stack.append(tree)
        while len(stack) > 0:
            # stack里面是栈，故而后进先出，append是后进，pop()是指pop出append里面的元素，pop(0)表示后入后出为队列
            root = stack.pop()
            self.result.append(root.val)
            # stack里面是栈，故而先压入右子树，再压入左子树
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return self.result

    def get_inorder(self, tree):
        """
        https://www.bilibili.com/video/BV1ub411A7hc/?spm_id_from=trigger_reload
        tree, iteration to complete
        :param tree:
        :return:
        """
        if tree is None:
            return None
        stack = []
        root = tree
        while root or len(stack) > 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                q = stack.pop()
                self.result.append(q.val)
                root = q.right
        return self.result

    def get_postorder(self, tree):
        """
        tree, iteration to complete
        https://www.bilibili.com/video/BV1up411R7NB?from=search&seid=3877660130804041690
        https://www.bilibili.com/video/BV13Z4y147My?from=search&seid=3877660130804041690
        :param tree: 根右左，再反转
        :return:
        """
        if tree is None:
            return None
        stack = [tree]
        while len(stack) > 0:
            root = stack.pop()
            self.result.append(root.val)
            # 栈后进先出，如果想得到根右左，必须左孩子先入栈
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return self.result[::-1]

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
    tree_traversal = Traversal()
    root = tree_traversal.create_tree()
    # 前序遍历 A、L、B、E、 C、D、W、X
    pre_order_result = tree_traversal.get_preorder(root)
    print(pre_order_result)
    # 中序遍历
    # B、L、E、A、 C、W、X、D
    tree_traversal = Traversal()
    root = tree_traversal.create_tree()
    in_order_result = tree_traversal.get_inorder(root)
    print(in_order_result)
    # 后序遍历
    # ['B', 'E', 'L', 'X', 'W', 'D', 'C', 'A']
    tree_traversal = Traversal()
    root = tree_traversal.create_tree()
    post_order_result = tree_traversal.get_postorder(root)
    print(post_order_result)