#给定一个无重复元素的正整数数组candidates和一个正整数target，
#找出candidates中所有可以使数字和为目标数target的唯一组合。
#candidates中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。

#回溯+剪枝
#画出树形图，然后深度优先遍历，找到满足条件的那一组路径，剪枝：将不满足条件的子树直接去除
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break

                dfs(candidates, index, size, path + [candidates[index]], res, residue)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res