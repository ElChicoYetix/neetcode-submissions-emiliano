# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        # once n == k...
        
        while cur or stack: # and
            while cur: # keep going left
                stack.append(cur)
                cur = cur.left
            
            # aqui cur es null, y haremos pop()
            cur = stack.pop()
            n += 1

            if n == k:
                return cur.val
            
            # ahora si podemos ir right
            cur = cur.right