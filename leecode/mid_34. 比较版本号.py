#版本号1：1.1.1        版本号2:1.1.2
#从前往后比，每一段可能有多位（001.002.001）
#版本号1<版本号2，返回-1
#版本号1>版本号2，返回1
#版本号1=版本号2，返回0

#双指针：定位每一段的开始和结尾
class Solution:
    def get_next_chunk(self, version: str, n: int, p: int) -> List[int]:
        # if pointer is set to the end of string
        # return 0
        if p > n - 1:
            return 0, p

        # find the end of chunk
        p_end = p
        while p_end < n and version[p_end] != '.':
            p_end += 1
        # retrieve the chunk
        i = int(version[p:p_end])
        # find the beginning of next chunk
        p = p_end + 1

        return i, p

    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)

        # compare versions
        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # the versions are equal
        return 0    