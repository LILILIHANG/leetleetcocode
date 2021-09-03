# m*n网格从左上角走到右下角的路径数，只能向右或向下走。
#动态规划，最后一步只能是从[i-1][j]或[i][j-1]走到
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp[i][j]表示到[i][j]位置的所有路径数
        #因为到第一行或第一列的位置均只有一条路径
        #初始化dp矩阵，第一行全赋值为1，第一列赋值为1
        dp=[[1]*n] + [[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

'''
求nums矩阵的最大路径和，
nums矩阵中每一个位置都有一个值，每一条路径和为路径上的值加和
dp[i][j]表示到达[i][j]位置的最大路径和
dp[i][j]=max(dp[i-1][j]+nums[i][j],dp[i][j-1]+nums[i][j])
'''