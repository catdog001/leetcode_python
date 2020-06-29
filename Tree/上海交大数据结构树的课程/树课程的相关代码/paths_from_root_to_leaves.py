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


class Paths(object):

    def __init__(self):
        self.result = []

    def get_paths(self, tree, single_path):
        """
        tree, iteration to complete
        :param tree:
        :return:
        """
        if tree is None:
            return
        single_path += int(tree.val)
        if not tree.left and not tree.right:
            self.result.append(single_path)
        else:
            self.get_paths(tree.left, single_path)
            self.get_paths(tree.right, single_path)


    def create_tree(self):
        A = TreeNode("1")
        L = TreeNode("2")
        B = TreeNode("3")
        C = TreeNode("5")
        A.left = L
        A.right = B
        L.right = C
        return A

    def get_paths_sum_result(self):
        return self.result


if __name__ == '__main__':
    single_path_sum = 0
    Path = Paths()
    tree = Path.create_tree()
    Path.get_paths(tree, single_path_sum)
    result = Path.get_paths_sum_result()
    print(result)


