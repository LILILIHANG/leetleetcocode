#rains中记录当前天是否下雨，不下雨记为0，下雨则记录下雨的池塘
#返回一个长度等于rains的数组，对应下雨天设为-1（不能进行任何操作），不下雨的天可以选择池塘抽水，记录抽水的池塘
#同一个池塘降雨超过两次就会溢出，避免溢出的情况出现

#从前往后遍历数组rains，存在需要抽水的池塘就向前找可以抽水的天，有则抽水，没有就返回[]
def func(rains):
    dic={}
    lst=[]
    res=[]
    for a, b in enumerate(rains):
        #当前天没有池塘下雨
        if not b:
            #res记录每天是否池塘降水，有记录为-1，没有记录为0
            res.append(b)
            #lst记录哪天不降水
            lst.append(a)
        #当前下雨的池塘之前也下过雨，所以需要对当前池塘抽水，需要找到当前池塘第一次降雨的天数dic[b]
        elif b in dic:
            #用来记录是否有需要抽水的池塘是否有不下雨的天可以抽水
            biaozhi=False
            #循环遍历lst中存的不下雨的天数
            for i ,j in enumerate(lst):
                #当前池塘第一次降雨的天数dic[b]之后有不下雨的天j
                if j>dic[b]:
                    lst.pop(i)
                    #将结果集res中对应天j的抽水池塘b记录下来
                    res[j]=b
                    #然后将当前下雨天在res中记录为-1
                    res.append(-1)
                    #在dic中记录当前池塘b下雨的天数
                    dic[b]=a
                    #处理完当前需要抽水的池塘，将标志位设为True
                    biaozhi=True
                    break
            #有需要抽水的池塘但是没有能够抽水的天，返回[]
            if not biaozhi:
                return []
        #当前池塘下雨，但是之前没下过
        else:
            #dic中只记录下雨天{哪个池塘：哪天下雨}
            dic[b]=a
            res.append(-1)
    #如果遍历完，res中存在0（不下雨的天没有进行任何抽水），则设为0
    for i, j in enumerate(res):
        if not j:
            res[i]=1
    return res