class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        
        memo = {}
        def dp(index, lastA, lastB) -> int:
            # returns the minimum swaps necessary
            # to ensure the array only increases
            # after this index
            if index == len(A):
                return 0
            
            key = str(index)+','+str(lastA)+','+str(lastB)
            if key in memo:
                return memo[key]
            
            
            # can continue without swapping
            if A[index]>lastA and B[index]>lastB:
                a = dp(index+1, A[index], B[index])
            else:
                a = float("inf")
            
            # can swap and continue
            if B[index]>lastA and A[index]>lastB:
                b = 1 + dp(index+1, B[index], A[index])
            else:
                b = float("inf")
            
            
            memo[key] = min(a,b)
            return memo[key]
                
        
        return dp(0,-1,-1)
                