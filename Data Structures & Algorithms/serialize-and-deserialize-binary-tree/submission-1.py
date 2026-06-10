# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        lista = []
        def deconstruir(root):
            if not root:
                lista.append("N")
            else: 
                lista.append(root.val)
                deconstruir(root.left)
                deconstruir(root.right)
        deconstruir(root)

        resultado = "".join(str(elemento) + "," for elemento in lista)
        print(resultado)

        return resultado
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        if data == "None,": return
        
        # ir guardando a la lista si no es ,
        # Elimina la coma sobrante al final y convierte a lista
        lista = data.rstrip(',').split(',')
        print(lista)

        # tener un switch indicando izq o der
        
        start = 0 # inicio de la lista
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
