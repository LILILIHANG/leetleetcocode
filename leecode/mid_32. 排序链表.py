#将链表排序

#1.自顶向下的归并排序：先分小段再归并排序
# 时间复杂度O(nlogn),空间复杂度O(nlogn)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        #将链表均分，直到每段链表只含有一个或两个节点
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))
        #归并排序每一小段链表
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)
#2.自下而上的归并排序：
#（1）用subLength表示每次需要排序的子链表的长度，初始时subLength=1。
#（2）每次将链表拆分成若干个长度为 subLength 的子链表（最后一个子链表的长度可以小于subLength），按照每两个子链表一组进行合并，
# 合并后即可得到若干个长度为 subLength×2 的有序子链表（最后一个子链表的长度可以小于 subLength×2）。
# 合并两个子链表仍然使用「21. 合并两个有序链表」的做法。
#（3）将subLength 的值加倍，重复第 2 步，对更长的有序子链表进行合并操作，直到有序子链表的长度大于或等于length，整个链表排序完毕。

# 时间复杂度O(nlogn),空间复杂度O(1)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                # 取第一段
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                #断开第一段
                curr.next = None
                # 取第二段
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    # 拿到第二段的下一个节点，断开第二段
                    succ = curr.next
                    curr.next = None
                # 合并前两段
                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                # 再从第三段开始，重复上述过程，合并接下来两段
                curr = succ
            # 将每个长度为subLength的小段合并结束后，再合并subLength*2的段
            subLength <<= 1

        return dummyHead.next