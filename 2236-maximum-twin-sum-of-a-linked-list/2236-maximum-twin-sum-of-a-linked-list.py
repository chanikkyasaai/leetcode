# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxsum = float("-inf")
        ls= [] 
        n = 0
        node = head
        while node:
            n+=1
            ls.append(node.val)
            node = node.next

        for i in range(n//2):
            maxsum = max(maxsum, ls[i]+ls[n-1-i])

        return 0 if maxsum == float('-inf') else maxsum

