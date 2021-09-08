'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
例如 'aaa'的回文字串数为：6
'''

'''
双指针法：确定回文串，就是找中心然后想两边扩散看是不是对称的
        一个元素可以作为中心点，两个元素也可以作为中心点。
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s))  # 以i为中心
            result += self.extend(s, i, i + 1, len(s))  # 以i和i+1为中心
        return result

    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res

s=Solution()
res=s.countSubstrings('aaa')
print(res)