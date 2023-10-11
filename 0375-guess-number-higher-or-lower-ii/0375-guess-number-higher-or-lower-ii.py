class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def rec(start,end):
            if start>=end:
                return 0
            ans=float('inf')
            for i in range(start,end+1):
                ans=min(ans,max(i+rec(start,i-1),i+rec(i+1,end)))
                
            return ans
        
        return rec(0,n)