class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#         q=[]
#         r,c=len(matrix),len(matrix[0])
#         for i,j in product(range(r),range(c)):
#             if matrix[i][j]==0:
#                 q.append((i,j))
                
        
#         for i,j in q:
#             for m in range(r):
#                 matrix[m][j]=0
#             for n in range(c):
#                 matrix[i][n]=0  
                
                
#         return matrix

        r,c=len(matrix),len(matrix[0])
        rowBool=False
        
        for i,j in product(range(r),range(c)):
            if matrix[i][j]==0:
                matrix[0][j]=0
                if i>0:
                    matrix[i][0]=0
                else:
                    rowBool=True
                    
                    
        for i,j in product(range(1,r),range(1,c)):
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j]=0
                
        if matrix[0][0]==0:
            for i in range(r):
                matrix[i][0]=0
            
            
        if rowBool:
            for j in range(c):
                matrix[0][j]=0
            
        return matrix