'''
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
'''

'''
动态规划
dp[i]以nums[i]结尾的最长连续字串和
dp[i]可由两部分得到：dp[i]=max(dp[i-1]+nums[i],nums[i])
1、dp[i-1]+nums[i]
2、重新计算字串和：nums[i]
'''
def maxSubArray(nums) -> int:
    if len(nums) == 0:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    result = dp[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 状态转移公式
        result = max(result, dp[i])  # result 保存dp[i]的最大值
    return result