
'''
# 给定一个数组 prices ，它的第i个元素prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
'''

'''
贪心算法，取到左边最小值
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            # 取最左最小价格
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit


'''
动态规划：比较难懂
dp[i][0]表示第i天持有股票所得最多现金,一开始现金是0，那么加入第i天买入股票现金就是 -prices[i]
    1、第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
    2、第i天买入股票，所得现金就是买入今天的股票后所得现金即：-prices[i]
    dp[i][0] = max(dp[i - 1][0], -prices[i])
dp[i][1]表示第i天不持有股票所得最多现金
    1、第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][1]
    2、第i天卖出股票，所得现金就是按照今天股票佳价格卖出后所得现金即：prices[i] + dp[i - 1][0]
    dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

初始化：
dp[0][0]表示第0天持有股票，此时的持有股票就一定是买入股票了，因为不可能有前一天推出来，所以dp[0][0] -= prices[0]
dp[0][1]表示第0天不持有股票，不持有股票那么现金就是0，所以dp[0][1] = 0
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if len == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[-1][1]