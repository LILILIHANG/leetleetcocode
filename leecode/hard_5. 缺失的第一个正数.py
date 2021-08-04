#题目：对于一个未排序的数组，返回给定数组中不存在的最小的正整数
#分析：对于一个长度为n的数组，返回的最小正整数只可能在[1，n+1]范围内
#     如果刚好包含1到n，则返回n+1；否则返回其中缺失的正整数。

#1，置换：遍历数组，将满足[1,n]的正整数i换到相应的位置nums[i-1]上
# 再遍历一遍数组，找到不属于[1,n]内的元素，返回它的下标-1即为缺失的正整数，否则返回n+1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            #and后的条件是为了避免限于无限交换的死循环
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
