#用户：李航
#开发时间：2021/4/16 21:41
#next迭代输出可迭代对象中的元素，配合iterate()将不可迭代对象转成可迭代对象

def reverseList(self, head):
    # 申请两个节点，pre和 cur，pre指向None
    pre = None
    cur = head
    # 遍历链表，while循环里面的内容其实可以写成一行
    # 这里只做演示，就不搞那么骚气的写法了
    while cur:
        # 记录当前节点的下一个节点
        tmp = cur.next
        # 然后将当前节点指向pre
        cur.next = pre
        # pre和cur节点都前进一位
        pre = cur
        cur = tmp
    return pre
