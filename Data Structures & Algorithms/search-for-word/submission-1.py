class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(row, col, i):
            if i == len(word): # todos los caracteres están
                return True 

            if (min(row, col) < 0 or # a la hora de buscar la letra, se pasa hacia arriba o izq del tablero
                row >= ROWS or col >= COLS or # rows o columns, están en el final
                word[i] != board[row][col] or # si la palabra no es la que estamos buscando
                (row, col) in path): # ya visitamos ese row, col

                return False

            path.add((row, col)) # agregamos el path vistiado, si no, luego hacemos pop()

            res = (backtrack(row + 1, col, i+1) or # arriba
                backtrack(row - 1, col, i+1) or # abajo
                backtrack(row, col - 1, i+1) or # izquierda
                backtrack(row, col + 1, i+1)) # derecha
            
            path.remove((row, col)) # pop()
            return res
        
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True
        return False