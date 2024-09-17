# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        node = head
        while node :
            l+=1
            node = node.next
        
        node = head
        ans = node
        count = 0
        if l-n+1 == 1:
            return ans.next
        while node and node.next:
            count+=1
            if count+1 == l-n+1:
                node.next = node.next.next
                break
                
            node = node.next

        return ans