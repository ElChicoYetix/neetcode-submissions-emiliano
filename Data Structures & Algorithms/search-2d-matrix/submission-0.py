class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #print("Valores en bloques", len(matrix[0])) # 4
        #print("Bloques", len(matrix)) # 3
        # print("Bloque num", valor // len(matrix[0])) # // 4
        # print("Valor numero", valor % len(matrix[0])) # % 4

        l, r = 0, len(matrix[0]) * len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            num_bloque = m // len(matrix[0])
            num_valor = m % len(matrix[0])

            if matrix[num_bloque][num_valor] > target:
                r = m - 1
                
            elif matrix[num_bloque][num_valor] < target:
                l = m + 1
                
            else:
                return True

        return False