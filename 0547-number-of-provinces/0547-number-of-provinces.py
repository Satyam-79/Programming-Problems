class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited=set()
        N=len(isConnected)
        
        def dfs(i):
            connections=isConnected[i]
            for j in range(N):
                if j not in visited and connections[j]==1 and i!=j:
                    visited.add(j)
                    dfs(j)
             
        Provinces=0
        for c in range(N):
            if c not in visited:
                Provinces+=1
                dfs(c)
        return Provinces
            