#从n个数的数组中选取满足目标和的k个数,数字可以无限制重复被选取。
class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        path = []
        def backtrack(candidates,target,sum,startIndex):
            if sum > target: return
            if sum == target: return res.append(path[:])
            for i in range(startIndex,len(candidates)):
                if sum + candidates[i] >target: return  #如果 sum + candidates[i] > target 就终止遍历
                sum += candidates[i]
                path.append(candidates[i])
                backtrack(candidates,target,sum,i)  #startIndex = i:表示可以重复读取当前的数
                sum -= candidates[i]  #回溯
                path.pop()  #回溯
        candidates = sorted(candidates)  #需要排序
        backtrack(candidates,target,0,0)
        return res
solution=Solution()
arr=[2,3,5]
res=solution.combinationSum(arr,8)
print(res)
"""
如果 target 减去一个数得到负数，那么减去一个更大的树依然是负数，同样搜索不到结果。
基于这个想法，我们可以对输入数组进行排序，添加相关逻辑达到进一步剪枝的目的；

链接：https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
"""