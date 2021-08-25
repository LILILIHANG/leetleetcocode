# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [start, end]。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
from typing import List


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key=lambda x: x[0])
#
#         merged = []
#         for interval in intervals:
#             # 如果列表为空，或者当前区间与上一区间不重合，直接添加
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#                 # 否则的话，我们就可以与上一区间进行合并
#                 merged[-1][1] = max(merged[-1][1], interval[1])
#
#         return merged

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            last = result[-1]
            if last[1] >= intervals[i][0]:
                result[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                result.append(intervals[i])
        return result
if __name__ == '__main__':
    nums = [[1,3],[2,4],[5,6]]
    solution = Solution()
    res = solution.merge(nums)
    print(res)