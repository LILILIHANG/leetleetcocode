# 给你一个字符串 s ，逐个翻转字符串中的所有单词 。
# 单词是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的单词分隔开。
# 请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。
# 输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
# 翻转后单词间应当仅用一个空格分隔。
# 翻转后的字符串中不应包含额外的空格。

#双指针，从后往前逐个搜索每个单词
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回