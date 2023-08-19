#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        #code here
        st,res=[],0
        for bar in histogram +[-1]:
            step=0
            while st and st[-1][1]>=bar:
                w,h=st.pop()
                step+=w
                res=max(res,step*h)
            st.append((step+1,bar))
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends