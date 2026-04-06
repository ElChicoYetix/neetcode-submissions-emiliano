class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        filas, columnas = len(matrix), len(matrix[0])

        top, bot = 0, filas - 1

        while top <= bot:
            fila = (top + bot) // 2

            if target > matrix[fila][-1]:
                top = fila + 1

            elif target < matrix[fila][0]:
                bot = fila - 1
            else:
                break
        
        if not (top <= bot):
            return False

        fila = (top + bot) // 2
        l, r = 0, columnas - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[fila][m]:
                l = m + 1
            elif target < matrix[fila][m]:
                r = m - 1
            else:
                
                return True
        
        return False