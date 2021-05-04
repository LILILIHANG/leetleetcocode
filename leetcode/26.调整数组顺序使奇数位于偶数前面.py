# 用户：李航
# 开发时间：2021/5/4 13:46

#1.辅助数组
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        item1=[]
        item2=[]
        for i in nums:
            if i%2==0:
                item1.append(i)
            else:
                item2.append(i)
        return  item2+item1

#双指针
#i从左向右找偶数，遇到奇数跳过
#j从右向左找奇数，遇到偶数跳过
#找到奇数和偶数时交换i，j
#i=j时退出
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums
