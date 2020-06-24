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
        self.height = 0

    def get_height(self, tree):
        """
        tree, recursive to complete
        :param tree:
        :return:
        """
        if tree is None:
            return 0
        left_height = self.get_height(tree.left)
        right_height = self.get_height(tree.right)
        return max(left_height, right_height) + 1

    def get_size(self, tree):
        """
        tree, recursive to complete
        :param tree:
        :return:
        """
        if tree is None:
            return 0
        if tree.left:
            print("tree.left is {}".format(tree.left.val))
        left_size = self.get_size(tree.left)
        print("left_size is {}".format(left_size))
        if tree.right:
            print("tree.right is {}".format(tree.right.val))
        right_size = self.get_size(tree.right)
        print("right_size is {}".format(right_size))
        return left_size + right_size + 1

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
    # 求树的高度
    height = tree_traversal.get_height(root)
    print("该树的高度是{}".format(height))
    # 求树的规模
    size = tree_traversal.get_size(root)
    print("该树的规模是{}".format(size))