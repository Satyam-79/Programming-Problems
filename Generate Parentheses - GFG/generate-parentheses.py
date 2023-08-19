#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        stack=[]
        res=[]
        def backTrack(start,end):
            if start == end == n:
                res.append(''.join(stack))
                return
            if start<n:
                stack.append('(')
                backTrack(start+1,end)
                stack.pop()
            if end<start:
                stack.append(')')
                backTrack(start,end+1)
                stack.pop()
            
        backTrack(0,0)
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends