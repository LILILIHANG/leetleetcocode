# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#滑动窗口：分别滑动A或B，找到重复子串的起始位置，将A与B对齐就可以遍历出字串长度。
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(A), len(B)
        ret = 0
        # 首先以A为基准，滑动B，从B开头依次对比A中对应位置元素，相等k+=1
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret, maxLength(i, 0, length))
        # 再以B为基准，滑动A，从A开头依次对比B中对应位置元素，相等k+=1
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret