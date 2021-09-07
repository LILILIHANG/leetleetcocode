'''
1
# m*n网格从左上角走到右下角的路径数，只能向右或向下走。
#动态规划问题
dp[i][j]为到[i][j]有多少条路径
最后一步只能是从[i-1][j]或[i][j-1]走到
'''
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
2
求nums矩阵的最大路径和，
nums矩阵中每一个位置都有一个值，每一条路径和为路径上的值加和
dp[i][j]表示到达[i][j]位置的最大路径和
dp[i][j]=max(dp[i-1][j]+nums[i][j],dp[i][j-1]+nums[i][j])
'''



'''
3
路径上有障碍物的情况，求有多少条路径

动态规划问题
dp[i][j]为到[i][j]有多少条路径
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        if dp[0][0] == 0: return 0

        # 第一行赋值，障碍物后的点不可达，设为0
        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]

        # 第一列赋值，障碍物后的点不可达，设为0
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[row - 1][col - 1]
