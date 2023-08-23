class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        res=1
        while num!=1:
            if num&1==1:
                res+=2
            else:
                res+=1
            num>>=1
        return res