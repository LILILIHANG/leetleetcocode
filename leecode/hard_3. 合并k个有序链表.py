# 给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。
#1,两两结合，分治
class Solution(object):
	def mergeKLists(self, lists):
		if not lists:
			return None
		# 通过mid将数组一分为二，并不断缩小规模，当规模为1时返回并开始合并
		# 通过合并两个链表，不断增大其规模，整体看就是不断缩小-最后不断扩大的过程
		def helper(begin,end):
			if begin==end:
				return lists[begin]
			mid = begin+(end-begin)/2
			left = helper(begin,mid)
			right = helper(mid+1,end)
			return merge(left,right)
		# 合并两个有序链表
		def merge(a,b):
			if not (a and b):
				return a if a else b
			if a.val<=b.val:
				a.next = merge(a.next,b)
				return a
			else:
				b.next = merge(a,b.next)
				return b
		return helper(0,len(lists)-1)

#最小堆排序
class Solution:
	def mergeKLists(self, lists):
		if not lists:
			return None
		import heapq
		queue = []
		dummy = ListNode(-1)
		cur = dummy
		# 遍历链表数组，然后将每个链表的每个节点都放入堆中
		for i in xrange(len(lists)):
			head = lists[i]
			while head:
				heapq.heappush(queue,(head.val,head))
				head = head.next
		# 从堆中不断取出元素，并将取出的元素串联起来
		while queue:
			_, cur.next = heapq.heappop(queue)
			cur = cur.next
		cur.next = None
		return dummy.next