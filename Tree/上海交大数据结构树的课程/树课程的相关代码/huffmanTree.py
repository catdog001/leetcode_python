"""
Huffman Tree used for compression
上海交大翁老师的：
https://www.bilibili.com/video/BV18t411U7tH?from=search&seid=14727695894489847315
青岛大学王卓老师的：
https://www.bilibili.com/video/BV18t411U7tz/?spm_id_from=trigger_reload
https://www.bilibili.com/video/BV18t411U7tz/?spm_id_from=trigger_reload
"""


class TreeNode(object):
    """
    节点类
    """
    def __init__(self, val="", weight=None):
        """

        :param left: 某一个节点的左孩子
        :param right: 某一个节点的右孩子
        :param val: 某一个节点的值，默认为空
        :param weight: 某一个节点的权重
        """
        self.father = None
        self.left = None
        self.right = None
        self.val = val
        self.weight = weight


class HuffmanTree(object):
    """
    Huffman Tree
    """
    def __init__(self, word_frequency):
        """

        :param word_frency: 字及其频率
        """
        self.word_frequency = word_frequency

    def create_huffman_tree(self):
        """
        依据词及其词频创建huffman树
        :return:
        """
        # 先采用优先队列对word_frency按低频到高频进行排列
        # 词和词的频次需要按(词的频次, 词)进行组合，python中的优先队列按(等级数字, 元素)中的等级数字进行排列，等级数字越小，优先级越高，越优先被弹出
        from queue import PriorityQueue
        word_frency_priority_queue = PriorityQueue()

        # （词频，词）放入优先队列进行排序
        for word_fre in self.word_frequency:
            word_frency_priority_queue.put(word_fre)

        # 每个词频建立以该词频为根的新树
        trees_priority_queue = PriorityQueue()
        while not word_frency_priority_queue.empty():
            new_ele = word_frency_priority_queue.get()
            new_ele_tree = TreeNode(val=new_ele[1], weight=new_ele[0])
            trees_priority_queue.put((new_ele_tree.weight, new_ele_tree))

        while trees_priority_queue.qsize() > 1:
            # 取出最小和次小, 最小做左节点，次小做右节点
            node_left = trees_priority_queue.get()[1]
            node_right = trees_priority_queue.get()[1]

            # 合并最小和次小，生成新的子树
            # 新的子树的左右节点为上述最小和次小的数值生成的节点
            father_node = TreeNode(weight=node_left.weight+node_right.weight)
            father_node.left = node_left
            father_node.right = node_right

            # 将最小和次小的删除，添加新的树节点。其实，对于优先队列来说，get方法是已经从优先队列中删除了
            # 新的树节点权重为 father_node.weight, 值默认为空

            # 设置父节点
            node_left.father = father_node
            node_right.father = father_node

            # 将新生成的子树的权重和值加入到优先队列中
            trees_priority_queue.put((father_node.weight, father_node))
        return trees_priority_queue.get()[1]

    def get_huffman_encode(self):
        """
        从huffman树拿到叶子结点的哈夫曼编码
        :return:
        """
        pass


if __name__ == '__main__':
    word_fre = [(10, "a"), (15, "e"), (12, "i"), (3, "s"), (4, "t"), (13, "d"), (1, "n")]
    huffman = HuffmanTree(word_fre)
    huffman_tree = huffman.create_huffman_tree()
    print(huffman_tree)







