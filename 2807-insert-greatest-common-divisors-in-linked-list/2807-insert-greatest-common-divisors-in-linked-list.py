# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1=head
        temp2=head.next
        while temp2!=None:
            temp=ListNode(math.gcd(temp1.val,temp2.val),temp1.next)
            temp1.next=temp
            temp1=temp2
            temp2=temp2.next
        return head