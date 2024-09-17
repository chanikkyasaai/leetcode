# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ln = 0
        node = head
        while node is not None:
            node = node.next
            ln+=1
        mid = math.ceil(ln/2)
        node = head
        for i in range(mid-1):
            node = node.next
        if ln%2 == 0:
            node = node.next
        return node
