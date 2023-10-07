class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        @cache
        def rec(idx,lastA,lastB):
            if idx==len(A):
                return 0
            a,b=float('inf'),float('inf')
            if A[idx]>lastA and B[idx]>lastB:
                a=rec(idx+1,A[idx],B[idx])
                
            if A[idx]>lastB and B[idx]>lastA:
                b=1+rec(idx+1,B[idx],A[idx])
                
            return min(a,b)
        
        return rec(0,-1,-1)
                