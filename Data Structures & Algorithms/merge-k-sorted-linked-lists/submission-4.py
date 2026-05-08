# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # si la lista está vacía, regresar None
        if not lists or len(lists) == 0:
            return None
        
        # seguir hasta que solo quede una lista final
        while len(lists) > 1:
            mergedLists = []  # aquí guardaremos las listas mergeadas

            # recorrer de 2 en 2
            for i in range(0, len(lists), 2): # subes de a 2 porq son pares.
                
                # primera lista
                l1 = lists[i]

                # migth be null, odd
                # segunda lista (puede no existir si hay número impar de listas)
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                # mergear ambas listas y guardar resultado
                mergedLists.append(self.mergeList(l1, l2))
            
            # actualizar lists con las listas ya mergeadas
            lists = mergedLists
        
        # al final solo queda una lista
        return lists[0]

    def mergeList(self, l1, l2):
        
        # nodo dummy para facilitar conexiones
        dummy = ListNode()
        
        # tail siempre apunta al final de la nueva lista
        tail = dummy

        # mientras ambas listas tengan nodos
        while l1 and l2:
            
            # tomar el nodo menor
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            # mover tail hacia adelante
            tail = tail.next

        # agregar los nodos restantes de l1
        if l1:
            tail.next = l1

        # agregar los nodos restantes de l2
        if l2:
            tail.next = l2
        
        # regresar la lista real (sin el dummy)
        return dummy.next