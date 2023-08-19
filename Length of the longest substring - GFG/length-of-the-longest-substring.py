#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, s):
        # code here
        max_len=0
        res=''
        for ele in s:
            if ele not in res:
                res+=ele
            else:
                res=res[res.index(ele)+1:]+ele
        
            if max_len<len(res):
                max_len=len(res)
        return max_len


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends