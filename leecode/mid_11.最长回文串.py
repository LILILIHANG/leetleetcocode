

#暴力法:从长度为2的字串开始判断
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]#用false填充n*n二维数组
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    #当边界i和j里面的字串也是回文串时(即dp[i + 1][j - 1]=true),(i,j)也是回文串
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len] #注意：左开右闭

#中心扩展法
#所有的回文串都是以长度为1或2的回文字串扩展开来的
# class Solution:
#     def expandAroundCenter(self, s, left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return left + 1, right - 1

#     def longestPalindrome(self, s: str) -> str:
#         start, end = 0, 0
#         for i in range(len(s)):
#             left1, right1 = self.expandAroundCenter(s, i, i)
#             left2, right2 = self.expandAroundCenter(s, i, i + 1)
#             if right1 - left1 > end - start:
#                 start, end = left1, right1
#             if right2 - left2 > end - start:
#                 start, end = left2, right2
#         return s[start: end + 1]
