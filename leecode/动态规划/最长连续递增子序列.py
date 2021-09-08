'''
求数组的最长连续递增子序列的长度
'''

'''
动态规划：dp[ i +1] = dp[i] + 1
'''
def findLengthOfLCIS(nums) -> int:
    if len(nums) == 0:
        return 0
    result = 1
    dp = [1] * len(nums)
    for i in range(len(nums)-1):
        #如果中间断了，还是从1开始累加，因为初始化的值为1
        if nums[i+1] > nums[i]:  # 连续记录
            dp[i+1] = dp[i] + 1
        result = max(result, dp[ i +1])
    return result
'''
贪心算法
'''
def findLengthOfLCIS(nums) -> int:
    if len(nums) == 0:
        return 0
    result = 1  # 连续子序列最少也是1
    count = 1
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:  # 连续记录
            count += 1
        else:  # 不连续，count从头开始
            count = 1
        result = max(result, count)
    return result