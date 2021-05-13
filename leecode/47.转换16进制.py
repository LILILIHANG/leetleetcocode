class Solution:
    def toHex(self, num: int) -> str:
        num &= 0xFFFFFFFF
        s = "0123456789abcdef"
        res = ""
        mask = 0b1111
        while num > 0:
            res += s[num & mask]
            num >>= 4
        return res[::-1] if res else "0"