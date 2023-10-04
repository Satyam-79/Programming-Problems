class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def rec(i,j):
            if i >=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            return rec(i+1,j)+rec(i,j+1)
        
        return rec(0,0)