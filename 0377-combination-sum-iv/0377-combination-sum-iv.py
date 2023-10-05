class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def rec(sums):
            if sums==target:
                return 1
            ans=0
            for num in nums:
                if sums + num <=target:
                    ans+=rec(sums+num)
            return ans
        
        return rec(0)
            