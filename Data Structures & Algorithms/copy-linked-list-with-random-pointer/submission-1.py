"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None : None }
        cur = head
        
        while cur:
            # Creamos una copia del nodo actual (solo con el valor)
            copy = Node(cur.val)
            
            # Guardamos la relación nodo original -> nodo copia
            oldToCopy[cur] = copy
            
            cur = cur.next
        
        cur = head
        # Segunda pasada: conectar los punteros next y random
        while cur:
            # Obtenemos la copia del nodo actual
            copy = oldToCopy[cur]
            
            # Asignamos el siguiente nodo usando el diccionario
            # (cur.next puede ser None, pero ya está cubierto en el diccionario)
            copy.next = oldToCopy[cur.next]
            
            # Asignamos el puntero random usando el diccionario
            copy.random = oldToCopy[cur.random]
            
            cur = cur.next

        return oldToCopy[head]

