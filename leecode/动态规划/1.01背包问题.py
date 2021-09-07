'''
01背包问题：有一个可装weight重量物品的背包，n件物品，每个物品都有重量和相应的价值
求背包最多可以装多少价值的物品？

动态规划问题：维护一个二维数组
dp[i][j]表示从 0-i个物品中选，放进容量为 j的背包
dp[i][j]=max(dp[i-1][j]+(dp[i-1][j-weight[i]]+value[i]))

dp[i-1][j]:第 i件物品装不下，所以dp[i][j]=dp[i-1][j]

dp[i-1][j-weight[i]]+value[i]:第 i件物品装得下，
dp[i - 1][j - weight[i]] 为背包容量为 j - weight[i]的时候不放物品i的最大价值，
那么dp[i - 1][j - weight[i]] + value[i] （物品i的价值），就是背包放物品i得到的最大价值
'''



def test_2_wei_bag_problem1(bag_size, weight, value) -> int:
    rows, cols = len(weight), bag_size + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    res = 0

    # 初始化dp数组,第一列均为0，
    for i in range(rows):
        dp[i][0] = 0
    first_item_weight, first_item_value = weight[0], value[0]
    #第一行背包容量>当前物品重量时，初始化为当前物品的价值
    for j in range(1, cols):
        if first_item_weight <= j:
            dp[0][j] = first_item_value

    # 更新dp数组: 先遍历物品, 再遍历背包.
    for i in range(1, len(weight)):
        cur_weight, cur_val = weight[i], value[i]
        for j in range(1, cols):
            if cur_weight > j:  # 说明背包装不下当前物品.
                dp[i][j] = dp[i - 1][j]  # 所以不装当前物品.
            else:
                # 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_val)
                if dp[i][j] > res:
                    res = dp[i][j]

    print(dp)
    print(res)


if __name__ == "__main__":
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    test_2_wei_bag_problem1(bag_size, weight, value)


'''
一维滚动数组实现，dp[j]表示背包容量为j时的最大可装价值物品
先遍历物品，再遍历背包容量，背包容量倒序遍历
'''
def test_1_wei_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)

    # 先遍历物品, 再遍历背包容量，避免每个背包只放入一个物品
    for i in range(len(weight)):
        #倒叙遍历背包容量，为了避免物品被重复放入
        for j in range(bag_weight, weight[i] - 1, -1):
            # 递归公式
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)

test_1_wei_bag_problem()