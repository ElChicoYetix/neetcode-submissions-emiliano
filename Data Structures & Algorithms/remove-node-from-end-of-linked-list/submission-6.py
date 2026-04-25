# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L, R = head, head
        
        # mover R n pasos
        for _ in range(n):
            R = R.next
        
        # ❗ si R es None → eliminar el primero
        if not R:
            return head.next

        # mover ambos hasta que R llegue al final
        while R.next:
            L = L.next
            R = R.next
        
        # ❗ eliminar nodo
        L.next = L.next.next
        
        return head