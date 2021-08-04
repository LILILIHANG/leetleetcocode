#给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
#你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
#返回滑动窗口中的最大值。

import heapq
def maxSlidingWindow(nums, k):
    n = len(nums)
    # 注意 Python 默认的优先队列是小根堆
    # 取负号后就变成大根堆
    q = [(-nums[i], i) for i in range(k)]
    heapq.heapify(q)
    #取堆顶元素
    ans = [-q[0][0]]
    for i in range(k, n):
        heapq.heappush(q, (-nums[i], i))
        #判断此时的堆顶元素（堆中最大元素）在不在当前窗口内，不在就pop出去，直到找到当前窗口中最大的元素
        while q[0][1] <= i - k:
            heapq.heappop(q)
        #将当前窗口最大元素加入到结果集中
        ans.append(-q[0][0])

    return ans
p=[3,1,4,6,2,5,7]
print(maxSlidingWindow(p,3))