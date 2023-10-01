class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        
        def rec(r,c):
            if r==len(triangle)-1:
                return triangle[r][c]
            if c>r:
                return float('inf')
            
            return triangle[r][c] + min(rec(r+1,c),rec(r+1,c+1))
        
        return rec(0,0)