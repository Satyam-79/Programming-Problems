# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
        
        
#         max_point=0
#         for i in range(len(points)):
#             count={}
#             count['a']=0
#             same_point=1
#             for j in range(i+1,len(points)):
#                 if points[i]==points[j]:
#                     same_point+=1
#                     continue
#                 if (points[j][0] - points[i][0])==0:
#                     m="inf"
#                 else:
#                     m = (points[j][1] - points[1][1]) / (points[j][0] - points[i][0])
#                 count[m]=count.get(m,0)+1
#             a=max(count.values())
#             max_point=max(max_point,a+same_point)
        
#         return max_point
        
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 0
        for i in range(len(points)):
            slopes = defaultdict(int)
            slopes['a'] = 0
            same_points = 1
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same_points += 1
                    continue
                slope = float('inf') if points[i][0] == points[j][0] else (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                slopes[slope] += 1
            a = max(slopes.values())
            max_points = max(max_points, a + same_points)
        return max_points