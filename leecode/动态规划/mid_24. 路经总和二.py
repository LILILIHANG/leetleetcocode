#给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点路径总和等于给定目标和的路径。
#叶子节点是指没有子节点的节点
#深度优先遍历
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = list()
        path = list()

        def dfs(root: TreeNode, targetSum: int):
            if not root:
                return
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                ret.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()

        dfs(root, targetSum)
        return ret
