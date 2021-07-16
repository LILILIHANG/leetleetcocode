# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）
# 后组成的新字符串。

#动态规划
# 定义 dp[i][j] 表示 text1[0:i-1] 和 text2[0:j-1] 的最长公共子序列。
# 1.当 text1[i - 1] == text2[j - 1] 时，说明两个子字符串的最后一位相等，所以最长公共子序列又增加了1，
# 所以 dp[i][j] = dp[i - 1][j - 1] + 1；
# 2.当 text1[i - 1] != text2[j - 1]时，说明两个子字符串的最后一位不相等，
# 那么此时的状态 dp[i][j] 应该是 dp[i - 1][j] 和 dp[i][j - 1] 中的最大值。


def longestCommonSubsequence(text1, text2):

    M, N = len(text1), len(text2)
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[M][N]

text1="abcde"
text2="bacad"

g=longestCommonSubsequence(text1,text2)
print(g)