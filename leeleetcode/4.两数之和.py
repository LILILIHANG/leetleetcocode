# 用户：李航
# 开发时间：2021/4/30 11:22
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num=len(nums)
        for i in range(num):
            for j in range(i+1,num):
                if nums[i]+nums[j]==target:
                    return (i,j)