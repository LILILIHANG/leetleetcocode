'''
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
# 你可以认为每种硬币的数量是无限的。
'''
from typing import List

'''
# 动态规划：完全背包问题
  dp[j]表示凑够 j 元的最小硬币数
  此题考虑组合顺序和不考虑组合顺序结果一样，所以无所谓先遍历物品还是背包
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        #先遍历物品
        for coin in coins:
            # 再遍历背包
            for j in range(coin, amount + 1):
                # 如果dp[x-coin]存在说明可以通过加上当前硬币达到目标和，同时总硬币数量加1
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

s=Solution()
res=s.coinChange([1,2,5],11)
print(res)
