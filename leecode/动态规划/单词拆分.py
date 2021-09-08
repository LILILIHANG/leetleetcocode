'''
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
'''
from typing import List

'''
完全背包问题
dp[i] : 字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词。
如果确定dp[j] 是true，且 [j, i] 这个区间的子串出现在字典里，那么dp[i]一定是true。（j < i ）。
初始化：dp[0]=true，无意义，只是为了保证后面结果，其他位置初始化为false
遍历顺序：本题还有特殊性，因为是要求子串，最好是遍历背包放在外循环，将遍历物品放在内循环。
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''排列'''
        dp = [False]*(len(s) + 1)
        dp[0] = True
        # 遍历背包
        for j in range(1, len(s) + 1):
            # 遍历单词
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])
        return dp[len(s)]

s=Solution()
res=s.wordBreak('leetcode',['leet','code'])
print(res)