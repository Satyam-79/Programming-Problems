class Solution:
    def numTilings(self, n: int) -> int:
        if n==0: return 0
        domino_cache={}
        tromino_cache={}
        
        def domino(t):
            dom={0:1,1:1,2:2}
            if t<=2:
                return dom[t]
            if t in domino_cache:
                return domino_cache[t]
            
            domino_cache[t] = (domino(t-2)+domino(t-1)+tromino(t-1)*2) % (10**9+7)
            return domino_cache[t]
            
        def tromino(t):
            tom={0:1,1:0,2:1}
            if t<=2:
                return tom[t]
            if t in tromino_cache:
                return tromino_cache[t]
            
            tromino_cache[t] = (domino(t-2)+tromino(t-1)) % (10**9+7)
            return tromino_cache[t]
        
        return domino(n) % (10**9+7)

# class Solution(object):
#     def numTilings(self, N):
#         if N==0: return 0
#         self.do, self.tro = {}, {}
#         return self.domino(N) % (10**9+7)
        
#     def domino(self, N):
#         dolow = {0:1, 1:1, 2:2}
#         if N<=2: return dolow[N]
#         if N in self.do: return self.do[N]
#         self.do[N] = self.domino(N-1) + self.domino(N-2) + self.tromino(N-1)*2
#         return self.do[N]
        
#     def tromino(self, N):
#         trolow = {0:1, 1:0, 2:1}
#         if N<=2: return trolow[N]
#         if N in self.tro: return self.tro[N]
#         self.tro[N] = self.domino(N-2) + self.tromino(N-1)
#         return self.tro[N]