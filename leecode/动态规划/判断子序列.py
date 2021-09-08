'''
判断字符串 s 是不是字符串 t 的子序列
'''

'''
dp[i][j]表示以 s[i-1]的字符串 s和以 t[i-1]的字符串 t的最长公共子序列的长度
'''

def isSubsequence(s: str, t: str) -> bool:
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            #dp[i][j]来源一
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # dp[i][j]来源二
            else:
                dp[i][j] = dp[i][j - 1]
    # s 和 t 的最长公共子序列长度=len(s)
    if dp[-1][-1] == len(s):
        return True
    return False