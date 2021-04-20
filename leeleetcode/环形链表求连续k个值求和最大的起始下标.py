# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#题目描述：输入包含n个元素的环形链表，顺时针（0,1,2,3，.....）循环求取连续k个值的最大的起始下标
#输入描述：
#第一行输入 n 和 k 分别表示数组有几个数和取连续k个数求和最大
#第二行输入 n 个数组元素 itme[0].......item[n-1]
#输出描述：
#输出从第几个数开始求和最大

import sys
x=sys.stdin.readline().strip()
m=list(map(int,x.split()))
n=m[0]
k=m[1]
x=sys.stdin.readline().strip()
m=list(map(int,x.split()))
maxtg=0
for j in range(n):
    temp=0
    for i in range(j,j+k):
        z=i
        if i>=n:
            z=z-n
        temp +=m [z]
        #z += 1
    a=maxtg
    maxtg=max(temp,maxtg)
    if a!=maxtg:
        b=i      #存取求和最大的一段的最后一个数的下标

#根据b往前找到这一段的起始值的下标
if b-k+1<0:  #末尾下标靠前时，往前找k个（b-k+1），起始下标为负（为倒数第几个），需要加上n+1变成正着数的下标，再加1输出正数第几个
    print(n+b-k+2)
else:        #末尾下标靠后时，往前找k个（b-k+1），起始下标为正直接+1输出是第几个数
    print(b-k+2)
