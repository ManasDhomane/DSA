
class Solution:
    def preorder(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            result.append(node.val)

            for child in node.children:
                dfs(child)

        dfs(root)
        return result