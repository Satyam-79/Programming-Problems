#User function Template for python3
import math
class Solution:
    def Solve(self, N, piles, h):
        # Code here
        maxEle = max(piles)
        l,r=1,maxEle
        res = r
        while l<=r:
            m=(l+r)//2

            hours = 0
            for p in piles:
                hours+=math.ceil(p/m)
            if hours<=h:
                res = min(m,res)
                r=m-1
            else:
                l=m+1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        piles = list(map(int, input().split()))
        H = int(input())
        ob = Solution()
        print(ob.Solve(N, piles, H))
# } Driver Code Ends