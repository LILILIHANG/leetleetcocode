# 用户：李航
# 开发时间：2021/5/2 22:08

# 给你二叉树的根节点root 和一个表示目标和的整数targetSum ，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和targetSum 。
#
# 叶子节点 是指没有子节点的节点。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)