'''
给你一个 只包含正整数的非空数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

01背包问题，背包容量为数组元素总和的一半，数组元素为物品重量和价值
dp[sum//2]==sum//2时表示可以分割成两个等和子集
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_=sum(nums)
        if sum_%2==1:return False
        target = sum_//2
        item_size=len(nums)
        dp=[0]*(target+1)
        for i in range(item_size):
            for j in range(target,nums[i]-1,-1):
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
        return target==dp[target]