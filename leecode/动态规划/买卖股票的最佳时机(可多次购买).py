'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。可多次购买股票
'''
'''
类似于单次购买股票，不同的是dp[i][0]的计算
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            #dp[i][0]：当第i天买入股票时，手里的现金为前天不持有股票手里的现金-今天购买股票的钱
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]) #注意这里是和单次买卖股票的最佳时机唯一不同的地方
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[-1][1]