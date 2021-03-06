#异位词：所含字母种类和数量相同
def isAnagram(s: str, t: str) -> bool:
    # 定义默认布尔值参与后续运算
    result = True
    # 利用 Python 数据结构 set 去重去序
    #将字符串放入哈希表就会去重
    set_tmp = set(s)
    # 先判断组成字符串的各个字符元素是否一致
    if set_tmp == set(t):
        for i in set_tmp:
            # 利用逻辑运算符判断各个字符元素的数量一致，均为 True 才输出 True
            result = result and (s.count(i) == t.count(i))
    else:
        result = False
    return (result)

s1='adadad'
s2='dadada'
a=isAnagram(s1,s2)
print(a)