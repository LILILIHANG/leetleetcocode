#给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#快慢指针：fast每次走两步，slow每次走一步，一定会相遇
# 设链表入环入口前有a个节点，环有b个节点，相遇时slow走了 nb 步，fast走了 2nb 步
# （推导：fast的步数是slow的两倍，f=2s，fast比slow多走n个环的步数，f=s+nb）
# 因为每当走到a+nb的步数时，都会到达环的入口，
# 所以在fast和slow第一次相遇后，将fast再从head开始每次走一步，当fast和slow再次相遇时走了a步，即在环形入口相遇

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast