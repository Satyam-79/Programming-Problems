class Solution:
    def countVowelPermutation(self, n: int) -> int:
        letters={'a':['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['i','u'],'u':['a']}
        
        @cache
        def rec(char,idx):
            if idx==n:
                return 1
            
            ans=0
            for c in letters[char]:
                ans+=rec(c,idx+1)%(10**9+7)
                
            return ans
        
        res=0
        for c in list(letters.keys()):
            res+=rec(c,1)%(10**9+7)
            
        return res%(10**9+7)