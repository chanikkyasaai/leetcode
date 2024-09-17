# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans

        while list1 and list2 :
            if list1.val <= list2.val:
                ans.next = list1
                list1 = list1.next
                
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next
        
        
        if list1 and not list2:
            ans.next = list1
        elif list2 and not list1:
            ans.next = list2

        
        return cur.next
