'''
题目要求：给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
'''

'''
动态规划问题
dp[i]为有i个节点的二叉搜索树的组合方式
解法：与节点上的数值无关，以4个节点为例，dp[4]可以分为以下几种情况：
1、以1为根节点，左子树有0个节点，右子树有3个节点，这种分配方式有dp[0]*dp[3]种组合方式
2、以2为根节点，左子树有1个节点，右子树有2个节点，这种分配方式有dp[1]*dp[2]种组合方式
3、以3为根节点，左子树有2个节点，右子树有1个节点，这种分配方式有dp[2]*dp[1]种组合方式
4、以4为根节点，左子树有3个节点，右子树有0个节点，这种分配方式有dp[3]*dp[0]种组合方式
dp[4]为以上四种情况求和
'''


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            #划分左右子树的节点数量，然后求累加
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]