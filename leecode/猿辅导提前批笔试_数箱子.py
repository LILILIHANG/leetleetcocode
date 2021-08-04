def longest(s: str):
    if not s:#输入为空
        return 0
    stack = []
    dep=0#记录深度，即现在所在的外层有多少括号
    depth=[]#记录每层深度的和，即每层括号里面的和
    for i in range(len(s)):
        if s[i] == '[':#遇到左括号深度+1
            stack.append(i)
            dep+=1
            depth.append(0)
        else:
            if i<len(s)-1 and s[i] == ']' and s[i+1] in '[]':#遇到右括号，深度-1，且右括号后没有数字，则可以直接当前深度箱子数量可直接加1
                stack.pop()
                dep-=1
                depth[dep]+=1
            elif i==len(s)-1 and s[i] == ']':#考虑边界情况，深度-1，当前深度箱子数量加1
                stack.pop()
                dep -= 1
                depth[dep] += 1
            elif s[i] == ']' and s[i+1] not in '[]':#遇到右括号，深度-1，右括号后有数字，则当前深度箱子数量可直接加num，且当前深度+1到最大深度每个深度都需要乘num
                num=int(s[i+1])
                dep -= 1
                depth[dep] += num
                for i in range(dep+1,len(depth)):
                    depth[i]=num*depth[i]
    return sum(depth)#每个深度箱子数量，即每个型号箱子个数相加

a="[][][[[]3[]2]2]2"
print(longest(a))

