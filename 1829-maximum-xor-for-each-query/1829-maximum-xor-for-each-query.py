class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        res=[0]*(n)
        maxBit=(2**maximumBit)-1
        xor=0
        for i in range(n):
            xor=xor ^ nums[i]
            res[n-1-i]=xor^maxBit
        return res
        