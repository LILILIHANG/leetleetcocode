# 快排思想
# 时间复杂度相比堆排序慢

class Solution:
    def findKthLargest(self, nums, k) -> int:
        # 第k个最大的元素，即升序排列后，index为len(nums)-k
        k = len(nums) - k
        low = 0
        high = len(nums) - 1
        while low <= high:
            p = self.patition(nums, low, high)
            if k < p:
                high = p-1
            elif k > p:
                low = p+1
            else:
                return nums[p]
        return -1


    def patition(self, alist, low, high):
        mid_value = alist[low]
        while low <high:
            while low < high and alist[high] >= mid_value:
                high -= 1
            alist[low] = alist[high]

            while low < high and alist[low] <= mid_value:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid_value
        return low