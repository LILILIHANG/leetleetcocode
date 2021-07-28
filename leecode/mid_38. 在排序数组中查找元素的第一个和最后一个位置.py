def searchRange(nums, target):
    if len(nums)==0:
        return [-1,-1]
    left=0
    right=len(nums)-1
    #二分法：找到目标元素的起始位置
    while left<right:
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        #相等时，右边界等于mid，不断向左推进，找到起始位置
        elif nums[mid]==target:
            right=mid
        else:
            right=mid-1
    #上面的二分法结束时的（left=right），没有找到目标，返回[-1,-1]
    if nums[left]!=target:
        return [-1,-1]
    #找目标元素的结束位置
    l2=left
    r2=len(nums)-1
    while l2<=r2:
        m2=(l2+r2)//2
        if nums[m2]==target:
            l2=m2+1
        elif nums[m2]>target:
            r2=m2-1
    return [left,l2-1]

nums=[5,7,7,8,8,10]
list=searchRange(nums,8)
print(list)