class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def rec(idx,buy):
            if idx>=len(prices):
                return 0
            if buy:
                return max(
                    -prices[idx]+rec(idx+1,0),
                    rec(idx+1,1)
                )
            return max(
                prices[idx]+rec(idx+2,1),
                rec(idx+1,0)
            )
            
        return rec(0,1)