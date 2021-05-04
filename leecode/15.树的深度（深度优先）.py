# 用户：李航
# 开发时间：2021/4/22 21:55
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_height=self.maxDepth(root.left)
            right_heigt=self.maxDepth(root.right)
        return max(left_height,right_heigt)+1