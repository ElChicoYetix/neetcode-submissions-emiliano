class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Solo agregar ( if open < n
        # Solo agregar ) if closed < open
        # valid if open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) # Unir en 1 string los valores del Stack
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)

                stack.pop() # pop al valor que acabamos de agregar

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)

                stack.pop()
        
        backtrack(0, 0)

        return res