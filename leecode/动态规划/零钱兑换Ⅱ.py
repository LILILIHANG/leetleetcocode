'''
给定不同面额的硬币和一个总金额。假设每一种面额的硬币有无限个。
写出函数来计算可以凑成总金额的硬币组合数。
'''

'''
动态规划：完全背包问题，背包容量正序遍历，此题需要先遍历物品再遍历背包，
不考虑组合元素顺序，即不会同时出现[1,3]和[3,1]
dp[j]表示凑够 j 元的方案数
'''
def change(coins,amount):
    dp=[1]+[0]*amount
    #遍历商品
    for i in range(len(coins)):
        #遍历背包容量，正序遍历，每个硬币可重复添加
        for j in range(coins[i],amount+1):
            dp[j]+=dp[j-coins[i]]
            print(dp)
        print('--------------')
    print(dp)

print('***********')
change([1,2,5],5)
