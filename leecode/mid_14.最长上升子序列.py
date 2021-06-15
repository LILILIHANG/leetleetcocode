#给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

#方法1：动态规划
class Solution:
def lengthOfLIS(List) -> int:
    if not List:
        return 0
    dp = []
    for i in range(len(List)):
        dp.append(1)
        for j in range(i):
            if List[i] > List[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


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

List=[10,9,2,5,3,7,101,18]
a=lengthOfLIS(List)
print(a)