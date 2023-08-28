class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def cal_days(weight):
            idx=0
            day=1
            w=0
            while idx<len(weights):
                if weight>=w+weights[idx]:
                    w+=weights[idx]
                    idx+=1
                else:
                    w=0
                    day+=1
                    if day>days:
                        return False
            return True

        l,r=max(weights),sum(weights)
        ans=0
        while l<=r:
            m=l+(r-l)//2
            if cal_days(m):
                r=m-1
                ans=m
            else:
                l=m+1
        return ans

            
        