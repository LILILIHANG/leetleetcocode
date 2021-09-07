#一趟扫描实现
#快慢指针：快指针比慢指针先走n步，快指针遍历完时，慢指针停在待删除节点前一个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
