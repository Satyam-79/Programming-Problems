class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         M,N = len(matrix)-1, len(matrix[0])-1
#         @cache
#         def rec(i,j):
#             val=matrix[i][j]
#             return 1+max(
#                 rec(i-1,j) if i and val>matrix[i-1][j] else 0,
#                 rec(i+1,j) if i < M and val>matrix[i+1][j] else 0,
#                 rec(i,j-1) if j and val>matrix[i][j-1] else 0,
#                 rec(i,j+1) if j < N and val>matrix[i][j+1] else 0,
#             )
        
#         ans=0
#         for r,c in product(range(M),range(N)):
#             ans=max(ans,rec(r,c))
            
#         return ans

            def dfs(i, j):
                if not dp[i][j]:
                    val = matrix[i][j]
                    dp[i][j] = 1 + max(
                        dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                        dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                        dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                        dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
                return dp[i][j]

            if not matrix or not matrix[0]: return 0
            M, N = len(matrix), len(matrix[0])
            dp = [[0] * N for i in range(M)]
            return max(dfs(x, y) for x in range(M) for y in range(N))