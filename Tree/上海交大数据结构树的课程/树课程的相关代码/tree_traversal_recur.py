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
        tree, recursive to complete
        :param tree:
        :return:
        """
        if tree is None:
            return None
        root = tree
        self.result.append(root.val)
        if root.left:
            self.get_preorder(root.left)
        if root.right:
            self.get_preorder(root.right)
        return self.result

    def get_inorder(self, tree):
        """
        tree, recursive to complete
        :param tree:
        :return:
        """
        if tree is None:
            return None
        root = tree
        if root.left:
            self.get_inorder(root.left)
        self.result.append(root.val)
        if root.right:
            self.get_inorder(root.right)
        return self.result

    def get_postorder(self, tree):
        """
        tree, recursive to complete
        :param tree:
        :return:
        """
        if tree is None:
            return None
        root = tree
        if root.left:
            self.get_postorder(root.left)
        if root.right:
            self.get_postorder(root.right)
        self.result.append(root.val)
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