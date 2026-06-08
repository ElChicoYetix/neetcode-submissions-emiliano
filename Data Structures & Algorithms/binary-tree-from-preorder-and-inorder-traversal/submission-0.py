# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # index del valor en Inorder

        # arbol izquierda, 1 -> mid # mid+1 incluye mid 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])   # preorder, inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:]) # preorder, inorder

        return root