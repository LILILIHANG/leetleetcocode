#例：输入‘A’，输出1
# 输入‘B’，输出2
# ...
# 输入‘Z’，输出26
# 输入‘AB’，输出28（1*26+2）
#ord()为转换成ASCⅡ码函数，reduce（a,b）对列表或元组b中的元素做函数a运算
import functools
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return functools.reduce(lambda x,y:x*26+y,[ord(i)-64 for i in columnTitle])