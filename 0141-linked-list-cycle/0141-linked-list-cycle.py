# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen = set()
        current = head
        while (current.next is not None) and (current.next not in seen):
            seen.add(current.next)
            current = current.next
        if current.next in seen:
            return True
        else:
            return False