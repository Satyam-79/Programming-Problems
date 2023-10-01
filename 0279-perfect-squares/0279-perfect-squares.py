class Solution:
    def numSquares(self, n: int) -> int:
#         i=2
#         squares=[1]
#         while squares[-1]<=n:
#             squares.append(i*i)
#             i+=1
            
#         if n in squares:
#             return 1
        
#         @cache
#         def rec(target):
#             if target==n:
#                 return 0
#             if target>n:
#                 return float('inf')
            
#             steps=float('inf')
#             for sq in squares:
#                 steps=min(steps,1+rec(target+sq))
                
#             return steps
                
        # return rec(0)
        @cache
        def solve(n):

            if n==0:                                                     # part 1
                return 0

            if n<0:                                                      # part 2
                return float("inf")

            mini = n                                                     # part 3 

            i = 1
            while i*i<=n:                                                # part 4
                mini = min(mini, solve(n-(i*i)))
                i+=1

            return mini+1                                                # part 5

        return solve(n)
                