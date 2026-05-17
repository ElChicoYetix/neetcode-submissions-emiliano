# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def treeHeight(root):
            if root is None: # Manejo de None
                return 0
            else:
                leftHeight = treeHeight(root.left)
                rightHeight = treeHeight(root.right)
                return 1 + max(leftHeight, rightHeight)

        if root is None:
            return True

        leftH = treeHeight(root.left)
        rightH = treeHeight(root.right)

        # revisar:
        # 1. nodo actual balanceado
        # 2. subárbol izquierdo balanceado
        # 3. subárbol derecho balanceado
        return (
            abs(leftH - rightH) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )