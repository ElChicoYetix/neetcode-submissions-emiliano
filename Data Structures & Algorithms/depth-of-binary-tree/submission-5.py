# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)): # eliminar valores en queue
                node = q.popleft()

                # Si el node tiene hijos
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # contando veces que queue es not empty
            level += 1
        
        return level