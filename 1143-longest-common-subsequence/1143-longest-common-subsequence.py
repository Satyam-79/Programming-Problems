class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def rec(i,j):
            if i>len(text1)-1 or j>len(text2)-1:
                return 0
            if text1[i]==text2[j]:
                return 1+rec(i+1,j+1)
            else:
                return max(rec(i+1,j),rec(i,j+1))
        
        return rec(0,0)