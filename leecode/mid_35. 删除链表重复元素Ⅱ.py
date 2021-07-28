#删除升序链表中所有的重复元素，例：[1,1,1,2,3]->[2,3]
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        #考虑头节点可能是重复节点
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next