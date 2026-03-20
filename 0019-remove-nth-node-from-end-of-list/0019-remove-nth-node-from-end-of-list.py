# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        fast = head 
        slow = dummyNode

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummyNode.next