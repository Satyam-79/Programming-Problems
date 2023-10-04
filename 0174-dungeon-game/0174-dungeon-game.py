class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @cache
        def rec(i,j):
            if i==len(dungeon)-1 and j==len(dungeon[0])-1:
                return max(1,-dungeon[i][j]+1)
            
            ans=float('inf')
            if i+1<len(dungeon):
                ans=min(ans,rec(i+1,j))
            if j+1<len(dungeon[0]):
                ans=min(ans,rec(i,j+1))
                
            ans+= -dungeon[i][j]
            
            return max(1,ans)
        
        return rec(0,0)
                