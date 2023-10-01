class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def rec(idx):
            if idx>=len(days):
                return 0
            
            min_cost=float('inf')
            for x,cost in zip((1,7,30),costs):
                temp=idx
                
                while temp<len(days) and x+days[idx] > days[temp]:
                    temp+=1
                min_cost=min(min_cost,cost+rec(temp))
                
            return min_cost
        
        return rec(0)