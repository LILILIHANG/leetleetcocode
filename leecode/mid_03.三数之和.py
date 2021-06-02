#返回数组中三数之和为0的三元组

#排序+双指针
# 1.特判，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
# 2.对数组进行排序。
# 3.遍历排序后数组：
#     （1）若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
#     （2）对于重复元素：跳过，避免出现重复解
#     （3）令左指针 L=i+1，右指针 R=n-1，当 L<R时，执行循环：
#     （4）当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
#         若和大于 0，说明 nums[R] 太大，R 左移
#         若和小于 0，说明 nums[L] 太小，L 右移
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res