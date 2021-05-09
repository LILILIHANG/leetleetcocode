#输入的数组为有序递增数组
#返回不重复的元素个数
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:#fast前面的数都不相同
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow