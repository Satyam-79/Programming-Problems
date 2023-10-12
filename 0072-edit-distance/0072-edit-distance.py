class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def rec(i,j):
            if i<0: 
                return j+1
            if j<0: 
                return i+1
            if word1[i]==word2[j]:
                return rec(i-1,j-1)
            return 1 + min(
                rec(i,j-1),
                rec(i-1,j),
                rec(i-1,j-1)
            )
        return rec(len(word1)-1,len(word2)-1)