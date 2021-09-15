class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def isCBT(head):
    if not head:
        return True
    isLeaf = False
    queue = []
    queue.append(head)
    while queue:
        head = queue.pop(0)
        left = head.left
        right = head.right
        if (not left and right) or (isLeaf and (left or right)):
            # （not left） and  right 右边存在 左边不存在
            #  或者是进入到全是叶节点状态后 有左或者右
            # 这两种情况都会返回F
            return False
        if left:
            queue.append(left)
        if right:
            queue.append(right)
        if not left or not right:
            isLeaf = True
    return True