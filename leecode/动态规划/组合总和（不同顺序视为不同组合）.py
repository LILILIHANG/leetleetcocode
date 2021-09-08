'''
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
请注意，顺序不同的序列被视作不同的组合。
'''

'''
完全背包问题，先遍历先遍历背包，再遍历商品会考虑组合中元素的顺序，[1,3]和[3,1]为两种不同的组合
dp[j]表示凑够 j 元的方案数
'''


def combinationSum4(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    #先遍历背包，再遍历商品会考虑组合中元素的顺序，[1,3]和[3,1]为两种不同的组合
    for i in range(1, target + 1):
        for j in coins:
            if i >= j:
                dp[i] += dp[i - j]

    return dp[-1]

res=combinationSum4([1,2,3],4)
print(res)

