# 用户：李航
# 开发时间：2021/4/29 10:48

#给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 [n/2] 的元素。
#摩尔投票法
# 根据上述的算法思想，我们遍历投票数组，将当前票数最多的候选人与其获得的（抵消后）票数分别存储在 major 与 count 中。
#
# 当我们遍历下一个选票时，判断当前 count 是否为零：
#
# 若 count == 0，代表当前 major 空缺，直接将当前候选人赋值给 major，并令 count++
# 若 count != 0，代表当前 major 的票数未被完全抵消，因此令 count--，即使用当前候选人的票数抵消 major 的票数

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major=0
        count=0
        for i in nums:
            if count==0:
                major=i
            if major==i:
                count+=1
            else:
                count-=1
        return major
