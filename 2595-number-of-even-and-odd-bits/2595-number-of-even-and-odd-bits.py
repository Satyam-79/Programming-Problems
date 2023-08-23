class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res=[0,0]
        i=0
        while n:
            if n&1==1:
                if i%2==0:
                    res[0]+=1
                else:
                    res[1]+=1
            n>>=1
            i+=1
            
        return res