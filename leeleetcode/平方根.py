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
