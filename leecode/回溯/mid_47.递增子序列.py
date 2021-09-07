
"""
求给定数组的递增子序列
"""

class Solution:
    def findSubsequences(self, nums):
        res = []
        path = []
        def backtrack(nums,startIndex):
            if len(path) >=2:
                res.append(path[:])  #注意这里不要加return，要取树上的节点
            for i in range(startIndex,len(nums)):
                if nums[i] in repeat:
                    continue
                if len(path) >= 1:
                    if nums[i] < path[-1]:
                        continue
                repeat.append(nums[i])  #记录这个元素在本层用过了，本层后面不能再用了
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        backtrack(nums,0)
        return res

solution=Solution()
arr=[2,6,2,4,7]
res=solution.findSubsequences(arr)
print(res)