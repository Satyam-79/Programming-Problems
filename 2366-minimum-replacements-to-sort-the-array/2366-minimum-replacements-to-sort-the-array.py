class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        last=nums[-1]
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>last:
                t=nums[i]//last
                if nums[i]%last:
                    t+=1
                last=nums[i]//t
                ans+=t-1
            else:
                last=nums[i]
        return ans