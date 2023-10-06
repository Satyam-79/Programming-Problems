class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4300:
            return 1.0
        @cache
        def rec(a,b):
            if a<=0 and b<=0:
                return 0.5
            if a<=0:
                return 1
            if b<=0:
                return 0
            
            prob=rec(a-100,b)+rec(a-50,b-50)+rec(a-75,b-25)+rec(a-25,b-75)
            
            return 0.25*prob
        
        
        return rec(n,n)
            