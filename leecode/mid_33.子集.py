#求无重复元素的数组的子集

#递归
def subsets(nums):
    res = []
    n = len(nums)

    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j + 1, tmp + [nums[j]])

    helper(0, [])
    return res
nums=[1,2,3]
list=subsets(nums)
#[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]