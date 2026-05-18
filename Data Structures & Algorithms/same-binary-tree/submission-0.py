# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left, right = [], []

        def dfs(root, lista):
            if not root:
                lista.append(101)
                return

            lista.append(root.val)

            dfs(root.left, lista)
            dfs(root.right, lista)

        dfs(p, left)
        dfs(q, right)

        print(left, right)
        
        return left == right