# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#广度优先搜索+设置奇偶层标志index
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        import collections
        # 定义一个双端队列，初始时候将根节点放入队列
        queue = collections.deque()
        queue.append(root)
        # 定义index，用来控制输出的方向的，是正向输出，还是反向输出
        index = 1
        res = []
        while queue:
            # 获取queue的长度，因为队列的长度是在不断变化的，这里需先确定要遍历多少次
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                # 如果左节点不为空，则继续放入队列中
                if node.left:
                    queue.append(node.left)
                # 如果右节点不为空，则继续放入队列中
                if node.right:
                    queue.append(node.right)
            # 当index为奇数时，就正向输出
            if (index & 1)==1:
                res.append(tmp)
            # 当index偶位数时，就反向输出，即先调用一次reverse，再保存
            else:
                res.append(tmp[::-1])
            index += 1
        return res