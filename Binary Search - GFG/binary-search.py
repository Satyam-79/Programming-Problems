#User function template for Python

class Solution:	
	def binarysearch(self, nums, n, target):
		# code here
		start=0
        end=len(nums)-1
        mid=(end+start)//2
        while mid>=start and mid<=end:
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
            mid=(end+start)//2
        return -1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends