# 给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
# k是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        cur = head
        while prev != tail:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head: #使用head作为终止条件是为了应对链表长度刚好被k整除的情况
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nexs = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nexs
            pre = tail
            head = tail.next

        return hair.next