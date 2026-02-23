class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                else:
                    left = dp[i][j-1]
                    up = dp[i-1][j]
                    dp[i][j] = left + up
        return dp[m-1][n-1]
                
# Tabulation
obj = Solution()
print(obj.uniquePaths(3,7))
        
        