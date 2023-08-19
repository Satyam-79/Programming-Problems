class Solution:
	def overlappedInterval(self, intervals):
		#Code here
		intervals.sort()
        i,j=0,0
        minI,maxI=float('inf'),float('-inf')
        res=[]
        while i<len(intervals):
            minI=intervals[i][0]
            maxI=intervals[i][1]
            j=i+1
            while j<len(intervals) and intervals[j][0]<=maxI:
                maxI=max(maxI,intervals[j][1])
                j+=1
            res+=[[minI,maxI]]
            i=j
        return res
        


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends