class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r=x^y
        res=0
        while r:
            r=r&(r-1)
            res+=1
        return res