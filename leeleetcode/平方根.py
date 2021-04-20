# 用户：李航
# 开发时间：2021/4/20 10:55

#二分查找法求平方根
def mysqrt(x):
    left,right,ans=0,x,-1
    while left<=right:
        mid=(left+right)//2
        if mid**2<=x:
            ans=mid
            left=mid+1
        else:
            right=mid-1
    print(ans)

mysqrt(12)

#转换成指数计算e^(0.5*lnx)
#def mySqrt(self, x: int) -> int:
#        if x == 0:
#            return 0
#        ans = int(math.exp(0.5 * math.log(x)))
##存在误差，需要判断ans和ans+1哪个是结果
#        return ans + 1 if (ans + 1) ** 2 <= x else ans
