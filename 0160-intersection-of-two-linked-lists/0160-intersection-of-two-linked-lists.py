# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        
        # brute force

        # while head1:
        #     node2 = head2
        #     while node2:
        #         if head1 == node2:
        #             return head1
        #         node2 = node2.next
        #     head1 = head1.next

        #optimal

        node = set()

        while head1:
            node.add(head1)
            head1 = head1.next
        
        while  head2:
            if head2 in node:
                return head2
            head2 = head2.next

        return None