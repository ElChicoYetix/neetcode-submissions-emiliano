# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        S, F = head, head.next
        while F and F.next:# is not null
            S = S.next
            F = F.next.next

        second = S.next # inicio de la segunda mitad
        S.next = None # Valor final / haces el split

        # Reverse Linked List
        """
        prev, curr = None, head 
        while curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        """

        prev = None

        while second:
            nxt = second.next
            second.next = prev 
            prev = second 
            second = nxt 

        # Al final del while, second = None, quiero que sea el final, el tail, por eso prev
        second = prev # Valor de la mitad (mitad más corta)
        first = head

        # Juntar ambas listas. Second half might be shorter
        while second:
            tmp1 = first.next 
            tmp2 = second.next 
            first.next = second 
            second.next = tmp1 

            first = tmp1 
            second = tmp2 
        
        return None