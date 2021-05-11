#输入一个二进制表示的整数，返回数字位数为‘1’的个数

# class Solution(object):
#     def hammingWeight(self, n):
#         return bin(n).count("1")

class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res