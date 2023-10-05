class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def rec(i,j):
            if obstacleGrid[i][j]==1:
                return 0
            if i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1:
                return 1
            ans=0
            if i+1<len(obstacleGrid) and obstacleGrid[i+1][j]!=1:
                ans+=rec(i+1,j)
            if j+1<len(obstacleGrid[0]) and obstacleGrid[i][j+1]!=1:
                ans+=rec(i,j+1)
                
            return ans
        
        return rec(0,0)