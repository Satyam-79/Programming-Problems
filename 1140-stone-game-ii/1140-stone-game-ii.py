class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N=len(piles)
        @cache
        def rec(start,M):
            if start>=N:
                return 0
            
            if N-start<=2*M:
                return sum(piles[start:])
            
            my_score=0
            total_score=sum(piles[start:])
            
            for x in range(1,2*M+1):
                opponent_score=rec(start+x,max(x,M))
                my_score=max(my_score,total_score-opponent_score)
                
            return my_score
        
        return rec(0,1)