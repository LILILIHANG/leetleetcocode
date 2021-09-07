# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
# 同一个节点在一条路径序列中至多出现一次 。该路径至少包含一个节点，且不一定经过根节点。

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxVal = root.val
        def dfs( root ):
            if not root:
                return 0
            left = max( 0, dfs( root.left ) )
            right = max( 0, dfs( root.right ) )
            self.maxVal = max( self.maxVal,  root.val + left + right )
            return root.val + max( left, right )
        dfs(root)
        return self.maxVal