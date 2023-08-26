class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=[""]*numRows
        i=0
        n=len(s)
        
        while i<n:
            j=0
            while j<numRows and i < n:
                res[j]+=s[i]
                j+=1
                i+=1
            j=numRows-2
            while j>0 and i < n:
                res[j]+=s[i]
                j-=1
                i+=1
        return ''.join(res)