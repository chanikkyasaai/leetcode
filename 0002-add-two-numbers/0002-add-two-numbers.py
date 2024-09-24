# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        nd = ans

        while (l1 or l2) or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum+= l2.val
                l2 = l2.next
            
            if carry:
                sum+= carry

            carry = sum // 10
            sum = sum%10

            node = ListNode(sum)
            nd.next = node

            nd = nd.next

        return ans.next