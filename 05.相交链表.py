# 用户：李航
# 开发时间：2021/4/30 11:23
# 编写一个程序，找到两个单链表相交的起始节点。
class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		a,b = headA,headB
		# 定义了两个节点a和b，只要a和b不等就继续遍历
		while a!=b:
			# 这步很关键，请对照动态图配合理解，
			#当a的下一个为空时，就a就从b链表头开始遍历
			a = a.next if a else headB
			# 同理，b也是类似的
			b = b.next if b else headA
		return a