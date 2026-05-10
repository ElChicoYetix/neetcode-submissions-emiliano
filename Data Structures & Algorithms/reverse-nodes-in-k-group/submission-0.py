# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        # 1 -> 2 -> 3 groupPrev es el 1
        # 1 -> 3 -> 2 groupPrev es el 1

        while True:
            kth = self.getKth(groupPrev, k) # last node in our group
            if not kth:
                break # si K no existe, ya llegamos al final lol

            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next # prev != None

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            nxt = groupPrev.next # first node in our group
            groupPrev.next = kth # poniendo kth al inicio
            groupPrev = nxt # update
        
        return dummy.next