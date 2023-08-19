#User function Template for python3

def Search(nums,n,target):
    #code here
    l,r=0,len(nums)-1
    res=float('inf')
    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            return m
        if nums[m]>=nums[l]:
            if nums[m]<target or target < nums[l]:
                l=m+1
            else:
                r=m-1
        else:
            if target<nums[m] or target> nums[r]:
                r=m-1
            else:
                l=m+1
    return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(Search(arr,n,k))

# } Driver Code Ends