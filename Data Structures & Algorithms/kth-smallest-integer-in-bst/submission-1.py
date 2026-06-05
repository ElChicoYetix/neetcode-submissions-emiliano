# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lista = []
        def dfs(root):
            if root is None:
                return
            lista.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        for i in range(1, k):
            minimo = min(lista)
            print(minimo)
            lista.remove(minimo)
        return min(lista)