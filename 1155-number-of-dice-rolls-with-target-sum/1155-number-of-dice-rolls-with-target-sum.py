class Solution:
    def numRollsToTarget(self, n: int, f: int, target: int) -> int:
        modulo=(10**9)+7
        @cache
        def rec(dice,target):
            if dice==0:
                return 0 if target>0 else 1
            res=0
            for k in range(max(0,target-f),target):
                res+=rec(dice-1,k)%modulo
            return res%modulo
        
        return rec(n,target)%modulo
        