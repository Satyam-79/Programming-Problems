class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def rec(i,total):
            if total==target and i==len(nums):
                return 1
            if i==len(nums):
                return 0
            return rec(i+1,total-nums[i])+rec(i+1,total+nums[i])
        
        return rec(0,0)
