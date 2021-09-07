# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
# 你可以认为每种硬币的数量是无限的。

# 动态规划：dp[s]=min(dp[s-coin])+1,s表示目标和，coin表示每一枚硬币
# 分别列除从最小硬币面值到目标和中间所有的dp[i],用于求解满足目标和的最小硬币
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            # 把每一个大于等于当前硬币面值，小于目标和的可能情况列出来
            for x in range(coin, amount + 1):
                # 如果dp[x-coin]存在说明可以通过加上当前硬币达到目标和，同时总硬币数量加1
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
