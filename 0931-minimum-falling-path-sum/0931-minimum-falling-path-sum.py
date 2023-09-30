class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def rec(i,j):
            if i>=len(matrix) or i<0 or j<0 or j>=len(matrix):
                return float('inf')
            if i==len(matrix)-1:
                return matrix[i][j]
            
            min_sum=float('inf')
            for x,y in ((1,1),(1,-1),(1,0)):
                min_sum=min(min_sum,rec(i+x,j+y))
                
            return matrix[i][j] + min_sum
        
        min_s=float('inf')
        for x in range(len(matrix)):
            min_s=min(min_s,rec(0,x))
            
        return min_s
            
            