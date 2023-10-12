class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @lru_cache(maxsize= 8000)
        def rec(first,second):
            if not first and not second:
                return ""
            if not first:
                return second
            if not second:
                return first
            if first[0]==second[0]:
                return first[0]+rec(first[1:],second[1:])
            one=first[0]+rec(first[1:],second)
            two=second[0]+rec(first,second[1:])
            
            if len(one)<len(two):
                return one
            return two
        return rec(str1,str2)