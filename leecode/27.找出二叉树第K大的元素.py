# 用户：李航
# 开发时间：2021/5/4 14:22

#二叉树中序遍历默认从小到大遍历元素，即left<root<right
# 打印中序遍历
# def dfs(root):
#     if not root: return
#     dfs(root.left)  # 左
#     print(root.val) # 根
#     dfs(root.right) # 右

# 打印中序遍历倒序(从大到小遍历)
# def dfs(root):
#     if not root: return
#     dfs(root.right) # 右
#     print(root.val) # 根
#     dfs(root.left)  # 左

def kthLargest(self, root: TreeNode, k: int) -> int:
    def dfs(root):
       if not root:
           return
       dfs(root.right)
       if self.k == 0:
           return
       self.k -= 1
       if self.k == 0:
           self.res = root.val
       dfs(root.left)
       self.k = k
       dfs(root)
       return self.res