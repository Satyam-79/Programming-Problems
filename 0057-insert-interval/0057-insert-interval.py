class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        l = bisect.bisect_left(intervals,newInterval[0],key=lambda r: r[1])
        r = bisect.bisect_right(intervals,newInterval[1],key=lambda r: r[0])
        
        if l < len(intervals):
            newInterval[0] = min(newInterval[0],intervals[l][0])
            
        if 0 < r:
            newInterval[1] = max(newInterval[1],intervals[r-1][1])
            
        return intervals[:l] + [ newInterval ] + intervals[r:]