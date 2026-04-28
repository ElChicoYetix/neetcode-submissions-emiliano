# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1:
            num = l1.val
            num1 = str(num) + num1
            l1 = l1.next

        while l2:
            num = l2.val
            num2 = str(num) + num2
            l2 = l2.next
        
        num1, num2 = int(num1), int(num2)
        suma = num1 + num2
        suma = str(suma)

        prev = None

        # Crear la lista ligada en reversa
        for i in range(len(suma)):
            nodo = ListNode(int(suma[i]))
            nodo.next = prev
            prev = nodo
        
        return prev  # head