'''
#给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列
'''


'''
#方法1：动态规划
dp[i]为以nums[i]为结尾的最长递增子序列的长度
'''
def lengthOfLIS(nums) -> int:
    if len(nums)<=1:return len(nums)
    dp = [1]*len(nums)
    res=0
    #外层为以nums[i]结尾的数组的最长递增子序列的长度
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        res=max(res,dp[i])
    return res


#方法2.贪心算法+二分法
#贪心：希望每次在上升子序列最后加上的那个数尽可能的小。
#思路：维护一个数组 d[i]，表示长度为 i 的最长上升子序列的末尾元素的最小值，用 len 记录目前最长上升子序列的长度。
def lengthOfLIS(nums) -> int:
    d = []
    for n in nums:
        #当前数大于d[-1]，更新最长子序列的长度，且以当前元素为末尾元素
        if not d or n > d[-1]:
            d.append(n)
        #当前数小于d[-1]，用二分法找到第一个比当前nums[i]小的数 d[k] ，并更新d[k+1]=nums[i]
        else:
            l, r = 0, len(d) - 1
            loc = r
            while l <= r:
                mid = (l + r) // 2
                if d[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            d[loc] = n
    #遍历完返回数组d的长度即为最长子序列的长度
    return len(d)

nums=[10,9,2,5,3,7,101,18]
a=lengthOfLIS(nums)
print(a)