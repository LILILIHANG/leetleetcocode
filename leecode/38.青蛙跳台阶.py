#青蛙一次可以跳一阶台阶或两阶台阶，问对于N个台阶有几种跳法
'''斐波那切数列，初始值不同'''
# class Solution:
#     def numWays(self, n: int) -> int:
#         a, b = 1, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a % 1000000007
# res=Solution()
# a=res.numWays(5)
# print(a)


'''每次可以跳1,2,3....m级台阶'''
def climbStairs(n,m):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n + 1):
        for j in range(1, m+1):
            if i >= j:
                dp[i] += dp[i - j]
    return dp[-1]

print(climbStairs(5,4))

'''
最小花费爬楼梯，爬每级台阶都需要花费相应的体力值，求爬上n级台阶的最小体力花费
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            #每次都取爬到当前楼梯的两种方式中最小体力消耗的方式，再加上当前台阶的体力消耗
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[len(cost)-1],dp[len(cost)-2])