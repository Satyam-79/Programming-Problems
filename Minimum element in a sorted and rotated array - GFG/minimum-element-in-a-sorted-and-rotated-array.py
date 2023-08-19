#User function Template for python3

class Solution:
    def findMin(self, nums, n):
        #complete the function here
        l,r=0,len(nums)-1
        min_ele=float('inf')
        while l<=r:
            if nums[l]<nums[r]:
                min_ele = min(min_ele,nums[l])
                break
            m=(l+r)//2
            min_ele = min(min_ele,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return min_ele


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends