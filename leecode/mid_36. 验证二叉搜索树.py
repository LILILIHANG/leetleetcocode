#二叉搜索树：如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值；
#          若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；它的左右子树也为二叉搜索树。

#1.递归
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False
            #右子树不为空，下界换为当前节点的值
            if not helper(node.right, val, upper):
                return False
            # 左子树不为空，上界换为当前节点的值
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

#2.中序遍历：左根右
#遍历下一个节点的时候判断是否大于上一个节点，是则继续，不是则返回false
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
