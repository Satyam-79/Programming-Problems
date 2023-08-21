class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q,visited=deque(),set()
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        level=1
        
        def isValid(row, col):
            if row >= len(mat) or row < 0 or col >= len(mat[0]) or col < 0:
                return False
            return True
        
        
        for i,j in product(range(len(mat)),(range(len(mat[0])))):
            if mat[i][j]==0:
                q.append([i,j])
                visited.add((i,j))
                
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for m,n in dirs:
                    newR,newC=r+m,c+n
                    if (newR,newC) not in visited and isValid(newR,newC):
                        visited.add((newR,newC))
                        q.append((newR,newC))
                        mat[newR][newC]=level
                        
            level+=1
            
        return mat
