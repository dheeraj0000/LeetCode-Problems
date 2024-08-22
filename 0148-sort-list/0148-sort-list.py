# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        a=[]
        while temp:
            a.append(temp.val)
            temp=temp.next
        a.sort()
        t=head
        for i in a:
            t.val=i
            t=t.next
        return head