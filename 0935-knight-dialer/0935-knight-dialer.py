class Solution:
    def knightDialer(self, n: int) -> int:
        dirs=((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
        @cache
        def rec(i,j,n):
            nonlocal dirs
            if i<0 or j<0 or i>=4 or j>=3 or (i==3 and j!=1):
                return 0
            if n==1:
                return 1
            ans=0
            for x,y in dirs:
                ans+=(rec(i+x,j+y,n-1)) % (10**9+7)
            
            return ans % (10**9+7)
        
        
        res=0
        for i in range(4):
            for j in range(3):
                res+=rec(i,j,n) % (10**9+7)
                
        return res % (10**9+7)