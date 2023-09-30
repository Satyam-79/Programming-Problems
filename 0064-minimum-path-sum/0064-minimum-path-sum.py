class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def rec(i,j):
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            
            if i==len(grid) or j==len(grid[0]):
                return float('inf')
            
            return grid[i][j] + min(rec(i+1,j),rec(i,j+1))
                       
        return rec(0,0)