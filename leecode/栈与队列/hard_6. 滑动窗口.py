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
#2、队列
class MyQueue: #单调队列（从大到小
        def __init__(self):
            self.queue = [] #使用list来实现单调队列

        #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
        #同时pop之前判断队列当前是否为空。
        def pop(self, value):
            if self.queue and value == self.queue[0]:
                self.queue.pop(0)#list.pop()时间复杂度为O(n),这里可以使用collections.deque()

        #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
        #这样就保持了队列里的数值是单调从大到小的了。
        def push(self, value):
            while self.queue and value > self.queue[-1]:
                self.queue.pop()
                self.queue.append(value)

        #查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
        def front(self):
            return self.queue[0]

class Solution:
        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            que = MyQueue()
            result = []
            for i in range(k): #先将前k的元素放进队列
                que.push(nums[i])
                result.append(que.front()) #result 记录前k的元素的最大值
            for i in range(k, len(nums)):
                que.pop(nums[i - k]) #滑动窗口移除最前面元素,pop中会判断，如果前面的元素已经在push的过程中被pop出去了，就不做任何操作
                que.push(nums[i]) #滑动窗口前加入最后面的元素
                result.append(que.front()) #记录对应的最大值
            return result