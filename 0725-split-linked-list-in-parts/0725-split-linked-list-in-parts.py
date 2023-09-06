# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        v=[None]*k
        length=0
        t=head
        while(t):
            t=t.next
            length+=1
            
        if length<=k:
            j=0
            while j<length:
                v[j]=head
                t=head.next
                head.next=None
                head=t
                j+=1
            return v
            
        extra=length % k
        i,j=0,0
        
        while i<k:
            j=0
            v[i]=head
            i+=1
            while j<(length//k)-1:
                head=head.next
                j+=1
            if extra:
                head=head.next
                extra-=1
            
            temp=head.next
            head.next=None
            head=temp
            
            
            
        return v
        