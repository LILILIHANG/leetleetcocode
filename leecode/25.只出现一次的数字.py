# 用户：李航
# 开发时间：2021/5/2 22:25


# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 如何才能做到线性时间复杂度和常数空间复杂度呢？
#
# 答案是使用位运算。对于这道题，可使用异或运算 \oplus⊕。异或运算有以下三个性质。
#
# 1.任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
# 2.任何数和其自身做异或运算，结果是 0，即 a ⊕ a=0。
# 3.异或运算满足交换律和结合律，即a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b
# 数组中的全部元素进行异或运算之后，出现两次的元素异或之后为0，最后只剩下出现一次的元素。

from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #reduce（function，数据集合） lambda为匿名函数（以x为自变量的函数，后面为函数体）
        # ^为异或运算
        return reduce(lambda x, y: x ^ y, nums)