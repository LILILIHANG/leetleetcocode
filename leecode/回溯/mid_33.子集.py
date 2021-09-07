"""
无重复元素数组的子集
"""

#递归
# def subsets(nums):
#     res = []
#     n = len(nums)
#
#     def helper(i, tmp):
#         res.append(tmp)
#         for j in range(i, n):
#             helper(j + 1, tmp + [nums[j]])
#
#     helper(0, [])
#     return res
# nums=[1,2,3]
# list=subsets(nums)
# print(list)
#[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

"""
有重复元素数组的子集，要求无重复的组合
回溯+剪枝：同一层不能使用相同的元素
"""
class Solution:
    def subsetsWithDup(self, nums):
        res = []  #存放符合条件结果的集合
        path = []  #用来存放符合条件结果
        def backtrack(nums,startIndex):
            res.append(path[:])
            for i in range(startIndex,len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:  #我们要对同一树层使用过的元素进行跳过
                    continue
                path.append(nums[i])
                backtrack(nums,i+1)  #递归
                path.pop()  #回溯
        nums = sorted(nums)  #去重需要排序
        backtrack(nums,0)
        return res
nums=[1,2,2,3]
solution=Solution()
list=solution.subsetsWithDup(nums)
print(list)