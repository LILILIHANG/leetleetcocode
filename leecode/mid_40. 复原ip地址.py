#给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
#有效 IP 地址:正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

#设定分区segId:(0,1,2,3)和每个分区的起始位置segStart和结束位置segEnd，遍历完当前分区，再调用dfs（segId + 1, segEnd + 1）遍历下一分区
#特殊情况：遍历到前导0；没找到4段ip就遍历完字符串
def restoreIpAddresses(s: str) -> str:
    SEG_COUNT = 4
    ans = []
    segments = [0] * SEG_COUNT

    def dfs(segId: int, segStart: int):
        # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
        if segId == SEG_COUNT:
            if segStart == len(s):
                ipAddr = ".".join(str(seg) for seg in segments)
                ans.append(ipAddr)
            return

        # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
        if segStart == len(s):
            return

        # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
        if s[segStart] == "0":
            segments[segId] = 0
            dfs(segId + 1, segStart + 1)

        # 一般情况，枚举每一种可能性并递归
        addr = 0
        for segEnd in range(segStart, len(s)):
            addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
            if 0 < addr <= 255:
                segments[segId] = addr
                dfs(segId + 1, segEnd + 1)
            else:
                break

    dfs(0, 0)
    return ans
