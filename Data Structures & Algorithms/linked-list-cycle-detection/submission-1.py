# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head # mueve 2 lugares
        slow = head # mueve 1 lugar

        while fast:
            if fast == None or fast.next == None or fast.next.next == None:
                return False

            fast = fast.next.next
            slow = slow.next

            if fast.next == slow or fast == slow: # si fast está detras o igual que slow
                return True
        return False