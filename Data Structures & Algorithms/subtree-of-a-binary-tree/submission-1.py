# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # string matching, hacerlo un str y ver si está?
        listaroot, listasubRoot = "", ""

        def dfs(root):
            if not root:
                return "None,"
            
            valor = str(root.val) + ","

            return (
                valor +
                dfs(root.left) +
                dfs(root.right)
            )

        listaroot = dfs(root)
        listasubRoot = dfs(subRoot)

        print(listaroot)
        print(listasubRoot)

        return listasubRoot in listaroot