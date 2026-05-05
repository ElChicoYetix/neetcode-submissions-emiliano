class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val  # guarda la llave y el valor del nodo
        self.prev = self.next = None   # punteros para lista doblemente ligada

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity            # capacidad máxima del cache
        self.cache = {} # map the key to nodes  # hashmap: key -> nodo

        # Left es LeastRecentlyUsed, right = MostRecentlyUsed
        # nodos dummy (sentinelas) para evitar edge cases
        self.left, self.right = Node(0, 0), Node(0, 0)
        
        # conectar los nodos dummy entre sí
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        # node is the middle one
        prev, nxt = node.prev, node.next  # obtener vecinos
        prev.next, nxt.prev = nxt, prev   # saltarse el nodo (lo desconecta)

    # insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right  # insertar antes del dummy right (MRU)
        
        # conectar nodo entre prev y nxt
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:  # si existe en el hashmap
            # TODO: update most recent
            # lo removemos de su posición actual
            self.remove(self.cache[key])
            
            # lo insertamos al final (MRU)
            self.insert(self.cache[key])

            return self.cache[key].val  # regresamos el valor
        
        return -1  # si no existe

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # si ya existe, removemos el nodo viejo (se va a reemplazar)
            self.remove(self.cache[key])
        
        # creamos un nuevo nodo y lo guardamos en el hashmap
        self.cache[key] = Node(key, value)
        
        # lo insertamos como el más recientemente usado
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # si excede la capacidad:
            # remove from the list and delete the LRU from the cache/hashmap
            
            lru = self.left.next  # el menos usado está justo después de left
            
            self.remove(lru)      # lo quitamos de la lista
            del self.cache[lru.key]  # lo eliminamos del hashmap