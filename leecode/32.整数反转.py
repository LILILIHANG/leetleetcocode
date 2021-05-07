
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围[−2^31, 2^31− 1] ，就返回 0。

#1.直接反转
# class Solution:
#     def reverse(self, x: int) -> int:
#         y, res = abs(x), 0
#         of = (1 << 31) - 1 if x > 0 else 1 << 31
#         while y != 0:
#             res = res * 10 + y % 10 #取到最后一位放到第一位
#             if res > of: return 0
#             y //= 10  #去掉最后一位（向下取整）
#         return res if x > 0 else -res

#2.转成字符串
def reverse(self, x: int) -> int:
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[:0:-1] #反向取到负号前一位
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0