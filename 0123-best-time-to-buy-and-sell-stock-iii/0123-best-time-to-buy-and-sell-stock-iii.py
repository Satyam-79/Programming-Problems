class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def rec(idx,buy,depth):
            if idx>=len(prices) or depth==0:
                return 0
            if buy:
                return max(
                    -prices[idx]+rec(idx+1,0,depth),
                    rec(idx+1,1,depth)
                )
            return max(
                prices[idx]+rec(idx+1,1,depth-1),
                rec(idx+1,0,depth)
            )
        
        return rec(0,1,2)