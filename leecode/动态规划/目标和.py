'''
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。
现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

例:nums=[1,1,1,1,1],S=3,输出：5
-1+1+1+1+1,+1-1+1+1+1,+1+1-1+1+1,+1+1+1-1+1,+1+1+1+1-1
'''

'''
动态规划：
sum(nums)，设所有正整数相加为x,则所有负整数相加为x-sum,要得到x+(x-sum)=S
可以推导出x=(sum+S)/2,问题转化为只要能凑出和为 x 的正数和，就能满足题意
则背包容量为 x

采用一维滚动数组，外层商品，内层背包容量且倒序
dp[j]：为装满j容量的背包有dp[j]种方法
dp[j] = dp[j] + dp[j - num]
当前填满容量为j的包的方法数 = 之前填满容量为j的包的方法数 + 之前填满容量为j - num的包的方法数
也就是当前数num的加入，可以把之前和为j - num的方法数加入进来。

'''
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumValue = sum(nums)
        #target > sumValue和背包容量为奇数时无解
        if target > sumValue or (sumValue + target) % 2 == 1: return 0
        #nums数组只有一个元素，例如[100],target=-200
        if len(nums) == 1 and nums[0] != abs(target): return 0
        bagSize = (sumValue + target) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagSize]
s=Solution()
res=s.findTargetSumWays([1,1,1,1,1],3)
print(res)
