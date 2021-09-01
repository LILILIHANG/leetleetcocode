class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def helper(root):
            if not root:
                return []

            for node in root.children:
                helper(node)

            res.append(root.val)

        helper(root)
        return res