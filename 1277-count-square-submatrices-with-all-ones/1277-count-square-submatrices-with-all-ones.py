class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dirs=((1,0),(0,1),(1,1))
        @cache
        def dfs(i,j):
            nonlocal dirs
            
            if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]==0:
                return 0
            ans=float('inf')
            for x,y in dirs:
                ans=min(ans,dfs(i+x,j+y)+1)
                
            return ans
        
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    res+=dfs(i,j)
                    
        return res