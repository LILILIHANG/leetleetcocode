#滑动窗口：分别滑动A或B，找到重复子串的起始位置，将A与B对齐就可以遍历出字串长度。
# class Solution:
#     def findLength(self, A: List[int], B: List[int]) -> int:
#         def maxLength(addA: int, addB: int, length: int) -> int:
#             ret = k = 0
#             for i in range(length):
#                 if A[addA + i] == B[addB + i]:
#                     k += 1
#                     ret = max(ret, k)
#                 else:
#                     k = 0
#             return ret
#
#         n, m = len(A), len(B)
#         ret = 0
#         # 首先以A为基准，滑动B，从B开头依次对比A中对应位置元素，相等k+=1
#         for i in range(n):
#             length = min(m, n - i)
#             ret = max(ret, maxLength(i, 0, length))
#         # 再以B为基准，滑动A，从A开头依次对比B中对应位置元素，相等k+=1
#         for i in range(m):
#             length = min(n, m - i)
#             ret = max(ret, maxLength(0, i, length))
#         return ret
'''
字串：连续，子序列：不连续
'''
'''
动态规划：
1、二维数组dp[i][j]:以下标i - 1为结尾的 A，和以下标j - 1为结尾的 B，最长重复子数组长度为dp[i][j].
    A[i-1] == B[j-1]时，dp[i][j] = dp[i - 1][j - 1] + 1
    
2、一维数组dp[j]：
'''
def findLength(A, B) -> int:
    if not A or not B:return 0
    dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
    res=0
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if A[i-1]==B[j-1]:
                #dp[i-1][j-1]表示以i-2和j-2结尾的A，B最长重复子串长度
                dp[i][j]=dp[i-1][j-1]+1
            res=max(res,dp[i][j])
    return res

a=findLength([1,2,3,2,1],[3,2,1,4,7])
print(a)