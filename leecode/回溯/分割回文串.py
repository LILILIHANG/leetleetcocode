'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
'''
'''
回溯法，设置子字符串的起始点startIndex，
从输出结果看：从字符串的后面向前不断增加回文字串的长度
'''


from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []  #放已经回文的子串
        def backtrack(s,startIndex):
            if startIndex >= len(s):  #如果起始位置已经大于s的大小，说明已经找到了一组分割方案了
                return res.append(path[:])
            for i in range(startIndex,len(s)):
                p = s[startIndex:i+1]  #获取[startIndex,i+1]在s中的子串
                if p == p[::-1]: path.append(p)  #是回文子串
                else: continue  #不是回文，跳过
                backtrack(s,i+1)  #寻找i+1为起始位置的子串
                path.pop()  #回溯过程，弹出本次已经填在path的子串
        backtrack(s,0)
        return res

s= Solution()
res=s.partition('aabbcdc')
print(res)