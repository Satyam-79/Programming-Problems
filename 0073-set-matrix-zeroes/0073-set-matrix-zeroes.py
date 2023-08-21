class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        q=[]
        r,c=len(matrix),len(matrix[0])
        for i,j in product(range(r),range(c)):
            if matrix[i][j]==0:
                q.append((i,j))
                
        
        for i,j in q:
            for m in range(r):
                matrix[m][j]=0
            for n in range(c):
                matrix[i][n]=0  
                
                
        return matrix