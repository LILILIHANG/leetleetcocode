#例:'abcabc':true  'aba':false

#1.枚举法
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):#子字符串的长度不会超过总长度的一半
            if n % i == 0:            #n一定是子字符串长度 i 的倍数
                if all(s[j] == s[j - i] for j in range(i, n)):#如果每个s[j]与第前i个字母s[j-i]相同，证明存在重复子字符串
                    return True
        return False
#2.自带查找函数
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)