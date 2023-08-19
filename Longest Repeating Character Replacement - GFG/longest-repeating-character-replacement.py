#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def characterReplacement(self, s, k):
        # Code here
        l,res=0,0
        count={}
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            if (r-l+1) - max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res =max(res,r-l+1)
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends