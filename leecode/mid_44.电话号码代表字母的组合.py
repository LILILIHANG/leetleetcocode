"""
2-9每个数字表示一个字符串的集合，
输入’23‘
输出2和3对应字符串中字母的组合
"""
class Solution:
    def letterCombinations(self, digits: str) :
        self.s = ""
        res = []
        letterMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if len(digits) == 0: return res
        def backtrack(digits,index):
            if index == len(digits):
                return res.append(self.s)
            digit = int(digits[index])  #将index指向的数字转为int
            letters = letterMap[digit]  #取数字对应的字符集
            for i in range(len(letters)):
                self.s += letters[i]
                backtrack(digits,index + 1)  #递归，注意index+1，一下层要处理下一个数字
                self.s = self.s[:-1]  #回溯
        backtrack(digits,0)
        return res

solution=Solution()
res=solution.letterCombinations('23')
print(res)