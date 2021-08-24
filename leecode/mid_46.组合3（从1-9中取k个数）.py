"""
从1-9中选k个和为n的数
每种组合中不允许有重复数字
"""

class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []  # 存放结果集
        path = []  # 符合条件的结果

        def findallPath(n, k, sum, startIndex):
            if sum > n: return  # 剪枝操作
            if sum == n and len(path) == k:  # 如果path.size() == k 但sum != n 直接返回
                return res.append(path[:])
            for i in range(startIndex, 9 - (k - len(path)) + 2):  # 剪枝操作
                path.append(i)
                sum += i
                findallPath(n, k, sum, i + 1)  # 注意i+1调整startIndex
                sum -= i  # 回溯
                path.pop()  # 回溯

        findallPath(n, k, 0, 1)
        return res

solution=Solution()
res=solution.combinationSum3(3,9)
print(res)