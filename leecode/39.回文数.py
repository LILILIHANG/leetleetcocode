#判断输入整数是否为回文数

#1.转成字符串，双指针
def isPalindrome(x: int) -> bool:
    lst = list(str(x))
    L, R = 0, len(lst) - 1
    while L <= R:
        if lst[L] != lst[R]:
            return False
        L += 1
        R -= 1
    return True

#2.不转成字符串，反转整数后半部分比较
def isPalindrome(x: int) -> bool:
    """
    只反转后面一半的数字!!(节省一半的时间)
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    elif x == 0:
        return True
    else:  #正数
        reverse_x = 0
        while x > reverse_x: #x的位数小于reverse_x的位数时
            remainder = x % 10
            reverse_x = reverse_x * 10 + remainder
            x = x // 10
        # 当x为奇数时, 只要满足 reverse_x//10 == x 即可
        if reverse_x == x or reverse_x // 10 == x:
            return True
        else:
            return False

x = 10
x = 100012
print(isPalindrome(x))