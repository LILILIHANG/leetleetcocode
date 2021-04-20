#输入元素个数为n的顺序排列1，2，.........  ，n，翻转k次，每次选择一个区间【a，b】进行翻转，求经过k次翻转之后形成的排列的逆序数？
#输入描述：
#第一行输入两个正整数 n 和 k
#接下来的 k 行每行输入两个正整数 a 和 b 
#输出：逆序数

import sys
# 读取第一行的n
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
n = values[0]
k = values[1]
nums=[]
for i in range(n):
    nums.append(i+1)
i = 0
for i in range(k):
# 读取每一行
    line = sys.stdin.readline().strip()
# 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    l = values[0]
    m = values[1]
    '''p = nums[l-1:m][::-1]'''
    a = (values[1]-values[0]+1)//2
    for j in range(a):
            temp = nums[l - 1]
            nums[l - 1] = nums[m - 1]
            nums[m - 1] = temp
            m = m -1
            l = l + 1
p = 0
print(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i]>nums[j]:
            p+=1
print(p)

