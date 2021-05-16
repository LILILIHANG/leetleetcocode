#计算求完阶乘之后的结果尾数有几个零
def count_zero(n):
    p=0
    while n>=5:
        n=n//5
        p+=n
    return p
a=count_zero(25)
print(a)