class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def rec(i,j):
            if i >= j:
                return False
            return max(
                piles[i] +rec(i+1,j),
                piles[j]+rec(i,j-1)
            )
        
        return rec(0,len(piles)-1)