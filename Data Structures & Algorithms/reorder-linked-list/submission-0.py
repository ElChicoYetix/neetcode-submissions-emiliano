# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ❗ ERROR: estabas moviendo head y lo perdías ✅ guarda referencia al inicio
        original = head

        lista = []

        # Crear lista
        while head:
            lista.append(head.val)
            head = head.next

        # Crear lista ordenada
        L, R = 0, len(lista) - 1
        res = []

        # ❗ ERROR: usabas L <= R → duplicaba el centro
        while L < R:
            res.append(lista[L])
            res.append(lista[R])
            L += 1
            R -= 1

        # ❗ FIX: si hay elemento en medio (caso impar), agrégalo una vez
        if L == R:
            res.append(lista[L])

        # ❌ ERROR: hacías head = res[0] (eso es int, no nodo)
        # ❌ ERROR: intentabas reconstruir nodos con ints en .next
        # ✅ FIX: NO tocar next, solo reasignar valores

        # utilizas el nodo original que da el problema, y como es misma len, solo cambias valores
        curr = original 
        i = 0

        while curr: 
            # ❗ ERROR: accedías res[i+1] → out of bounds
            # ✅ FIX: solo usa res[i]
            curr.val = res[i]
            curr = curr.next
            i += 1

        return None