#青蛙一次可以跳一阶台阶或两阶台阶，问对于N个台阶有几种跳法
#斐波那切数列，初始值不同
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
