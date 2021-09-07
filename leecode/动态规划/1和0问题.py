'''
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3 输出：4
返回strs 的最大子集的大小，该子集中 最多有 m 个 0 和 n 个 1。

解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。
{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
'''

'''
二维数组dp[i][j]:表示最多有i个0和j个1时，最大子集的大小
dp[i][j]=max(dp[i][j], dp[i - zeros][j - ones] + 1)
dp[i - zeros][j - ones] + 1表示加入当前遍历的字符串后，子集的大小等于刨去当前字符串的0和1的dp[i - zeros][j - ones]，再加上1
即在上一次最大的dp[i][j]和加入当前物品后的子集大小中取最大值
'''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]	# 默认初始化0
        # 遍历物品
        for str in strs:
            ones = str.count('1')
            zeros = str.count('0')
            # 遍历背包容量且从后向前遍历，避免重复添加
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]