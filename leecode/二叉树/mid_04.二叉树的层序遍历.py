
#from queue import Queue 引入队列模块
# q=Queue(maxsize=5)
# for i in range(5):
#     q.put(i)
# print(q.get())

#BFS：广度优先搜索
#用列表实现队列，未使用队列模块
class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res = []
		queue = [root]
		while queue:
			# 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
			size = len(queue)
			tmp = []
			# 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
			# 如果节点的左/右子树不为空，也放入队列中
			for _ in range(size):
				r = queue.pop(0)
				tmp.append(r.val)
				if r.left:
					queue.append(r.left)
				if r.right:
					queue.append(r.right)
			# 将临时list加入最终返回结果中
			res.append(tmp)
		return res

#DFS：深度优先搜索
class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res = []
        #从上到下按照每一层（index代表层数）都先填充一个空列表到res，然后从上到下深度遍历每次填充一个元素到对应层的列表中，直到每一层的元素都添加完成
		def dfs(index,r):
			# 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
			if len(res)<index:
				res.append([])
			#  将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
			# res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
			res[index-1].append(r.val)
			# 递归的处理左子树，右子树，同时将层数index+1
			if r.left:
				dfs(index+1,r.left)
			if r.right:
				dfs(index+1,r.right)
		dfs(1,root)
		return res