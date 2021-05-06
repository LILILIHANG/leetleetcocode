
#将数组中的所有非零元素移动到数组左侧且不改变顺序
#1
class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		if not nums:
			return 0
		# 第一次遍历的时候，j指针记录非0的个数，只要是非0的统统都赋给nums[j]
		j = 0
		for i in xrange(len(nums)):
			if nums[i]:
				nums[j] = nums[i]
				j += 1
		# 非0元素统计完了，剩下的都是0了
		# 所以第二次遍历把末尾的元素都赋为0即可
		for i in xrange(j,len(nums)):
			nums[i] = 0
#2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1