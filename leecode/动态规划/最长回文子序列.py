'''
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。
'''

'''
dp[i][j]：字符串s在[i, j]范围内最长的回文子序列的长度为dp[i][j]。

递推公式:
s[i]==s[j]，dp[i][j] = dp[i + 1][j - 1] + 2
s[i]！=s[j]，dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

遍历顺序：从下到上遍历对角线右上的元素
'''


def longestPalindromeSubseq(s: str) -> int:
    dp = [[0] * len(s) for _ in range(len(s))]
    #初始化对角线为1，对角线表示单个字符为回文串
    for i in range(len(s)):
        dp[i][i] = 1
    #从下向上遍历对角线右上角的元素
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][len(s)-1]

res=longestPalindromeSubseq('bbbab')
print(res)