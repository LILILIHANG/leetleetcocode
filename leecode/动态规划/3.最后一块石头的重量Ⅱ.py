'''
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
每一回合，从中选出任意两块石头，然后将相撞，相撞之后的石头重量为二者之差。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
'''

'''
将石头总重量的一半设为背包最大容量，target=sum//2
利用分割等和子集的方法，将石头分成近似相等的两堆
求dp[target],因为//是向下取整，所以sum-dp[target]>=dp[target]
从两堆石头中各选一块相撞，最后剩下的石头的重量为(sum-dp[target])-dp[target]
'''



class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumweight = sum(stones)
        target = sumweight // 2
        dp = [0] * 15001
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return (sumweight - dp[target])- dp[target]