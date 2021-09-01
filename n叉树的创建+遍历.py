class Node():
    # 初始化一个节点
    def __init__(self,val = None):
        self.val = val       # 节点值
        self.l_child = []    # 子节点列表
    # 添加子节点
    def add_child(self,node):
        self.l_child.append(node)

root = Node('A')
B = Node('B')
root.add_child(B)
root.add_child(Node('C'))
D = Node('D')
root.add_child(D)
B.add_child(Node('E'))
B.add_child(Node('F'))
B.add_child(Node('G'))
D.add_child(Node('H'))
D.add_child(Node('I'))

res = ''

def pre(tn):
    global res
    if not tn:
        return
    res += tn.val
    for i in tn.l_child:
        pre(i)
    return(res)

pre(root)
print(res)
