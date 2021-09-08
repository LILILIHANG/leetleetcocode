'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
输出组成和为 n 的最少完全平方数的个数。
'''

'''
完全背包问题：无所谓先遍历商品还是背包
dp[j]表示合为 j 的最少完全平方数的个数 
'''
class Solution:
    def numSquares(self, n: int) -> int:
        #生成完全平方数的序列
        nums=[i**2 for i in range(1,n+1) if i**2<=n]
        dp=[0]+[float('inf')]*n
        for i in nums:
            for j in range(i,n+1):
                dp[j]=min(dp[j],dp[j-i]+1)
        return dp[-1]

s=Solution()
res=s.numSquares(3)
print(res)