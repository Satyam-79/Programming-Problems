class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        heap=[[-v,e] for e,v in count.items()]
        heapify(heap)
        
        i=0
        n=len(s)
        ans=['']*n
        
        while heap:
            v,e=heap.pop(0)
            v=-v
            if 2*v-1 > n:
                return ''
            for _ in range(v):
                ans[i]=e
                i=i+2 if i+2<n else 1
                
        return ''.join(ans)
            