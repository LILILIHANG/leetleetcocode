"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以按任意顺序返回答案。
"""

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  #存放符合条件结果的集合
        path = []  #用来存放符合条件的结果
        used = []  #用来存放已经用过的数字
        def backtrack(nums,used):
            if len(path) == len(nums):
                return res.append(path[:])  #此时说明找到了一组
            for i in range(0,len(nums)):
                if nums[i] in used:
                    continue  #used里已经收录的元素，直接跳过
                path.append(nums[i])
                used.append(nums[i])
                backtrack(nums,used)
                used.pop()
                path.pop()
        backtrack(nums,used)
        return res

if __name__ == '__main__':
    nums = [1, 2, 3,4]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
"""
给定一个含重复数字的数组 nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。
需要去重：同一层的相同的元素需要剪枝
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # res用来存放结果
        if not nums: return []
        res = []
        used = [0] * len(nums)
        def backtracking(nums, used, path):
            # 终止条件
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtracking(nums, used, path)
                    path.pop()
                    used[i] = 0
        # 记得给nums排序
        backtracking(sorted(nums),used,[])
        return res
if __name__ == '__main__':
    nums = [1, 2,2, 3,4]
    solution = Solution()
    res = solution.permuteUnique(nums)
    print(res)