class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @cache
        def rec(idx,even):
            if idx==len(nums):
                return 0
            
            val =-1
            if even:
                val=1
            
            pick = nums[idx]*(val) + rec(idx+1,not even)
            not_pick=rec(idx+1,even)
            
            return max(pick,not_pick)
        return rec(0,True)