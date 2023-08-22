class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        n=len(s)
        @cache
        def dfs(a,i):
            if i==n:
                res.append(a)
                return
            if 'a'<=s[i]<='z':
                dfs(a+s[i].upper(),i+1)
            elif 'A'<=s[i]<='z':
                dfs(a+s[i].lower(),i+1)
            dfs(a+s[i],i+1)
            
        dfs("",0)
        return res
            
            