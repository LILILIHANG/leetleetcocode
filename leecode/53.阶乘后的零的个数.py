#计算求完阶乘之后的结果尾数有几个零
#只需找出所有阶乘数字的因子中有几对2和5，又由于对于任意一个数字2的因子个数总是大于5的个数，所以只需统计5的个数
def count_zero(n):
    p=0
    while n>=5:
        n=n//5
        p+=n
    return p
a=count_zero(25)
print(a)
