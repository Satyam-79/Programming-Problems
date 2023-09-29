class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        @cache
        def rec(p1,p2,i):
            if p1==p2:
                return True
            if i>=len(nums):
                return False
            
            return rec(p1+nums[i],p2-nums[i],i+1) or rec(p1,p2,i+1)
        
        return rec(0,sum(nums),0)