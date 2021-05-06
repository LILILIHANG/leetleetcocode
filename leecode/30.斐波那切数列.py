#返回斐波那切数列的第N个值F（n），F(0)=0,F(1)=1
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a%1000000007