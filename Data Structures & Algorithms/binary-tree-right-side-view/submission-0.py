# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root]) # puede tener un null mi queue

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()

                if node: # actualizas rightSide, seria el ultimo
                    rightSide = node 
                    # tomas hijos
                    q.append(node.left) # el orden importa
                    q.append(node.right)

            # ya tomaste los nodos y sus hijos, ahora
            # remove nums from prev level and added nums from next level
            if rightSide:
                res.append(rightSide.val)
        
        return res