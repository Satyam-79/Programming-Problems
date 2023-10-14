class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def rec(total,idx):
            if total==amount:
                return 1
            if total>amount or idx==len(coins):
                return 0
            ans= rec(total+coins[idx],idx)+rec(total,idx+1)
            return ans
        return rec(0,0)