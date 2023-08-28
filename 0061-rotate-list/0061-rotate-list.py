# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k==0:
            return head
        left=right=head
        length=1
        count=0
        while right.next:
            right=right.next
            length+=1
        # print(length)
        k = k % length
        # print(k)
        if k==0 or length==1:
            return head
        
        for _ in range(length-k-1):
            left=left.next
            
        temp=left.next
        left.next=None
        right.next=head
        return temp
            
                
        
        