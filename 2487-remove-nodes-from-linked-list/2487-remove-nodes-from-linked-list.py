# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if not head.next:
            return head
        
        def rec(temp):
            if not temp:
                return None
                
            temp.next=rec(temp.next)
            return temp.next if (temp.next != None and temp.val<temp.next.val) else temp
            
            
        return rec(temp)
            
        