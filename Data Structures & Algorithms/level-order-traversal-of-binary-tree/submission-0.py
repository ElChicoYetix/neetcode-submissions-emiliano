# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def treeHeight(root):
            if root is None:
                return 0
            else:
                leftHeight = treeHeight(root.left)
                rightHeight = treeHeight(root.right)
                return 1 + max(leftHeight, rightHeight)
        
        res = treeHeight(root)

        resultado = [[] for _ in range(res)]

        def dfs(root, resultado, nivel):
            if not root:
                return

            # agregar al nivel correspondiente
            resultado[nivel].append(root.val)

            # hijos estarán un nivel abajo
            dfs(root.left, resultado, nivel + 1)
            dfs(root.right, resultado, nivel + 1)

        dfs(root, resultado, 0)

        return resultado