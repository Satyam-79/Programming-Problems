class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
            