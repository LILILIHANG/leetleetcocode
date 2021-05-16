#二叉搜索树：按照左>根>右的大小进行建树
#找出任意两节点的最小句绝对值差
#采用中序遍历，得到递增序列

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        st = []
        p = root
        pre = -float('inf')
        min_val = float('inf')
        while p is not None or st:
            while p is not None:
                st.append(p) #按照中序遍历得到递增序列
                p = p.left
            p = st.pop()
            cur = p.val
            if cur - pre < min_val:
                min_val = cur - pre
            pre = cur
            p = p.right
        return min_val