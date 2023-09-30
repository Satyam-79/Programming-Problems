class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        #ans=min(y-x)   y=(stone[.+.+.]) & x=(stone[.+.+.])
        @cache
        def rec(target,i,x):
            if target<x:
                return 0
            if i==len(stones):
                return x
            return max(rec(target,i+1,x+stones[i]),rec(target,i+1,x))
            
            
            
        total_stones_wt=sum(stones)
        x=rec((total_stones_wt//2),0,0)
        return total_stones_wt-(2*x)