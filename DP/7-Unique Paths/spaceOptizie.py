class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[0] * n
        for i in range(m):
            left = 0
            for j in range(n):
                if i == 0 :
                    dp[j] = 1
                    continue
                else:
                    dp[j]=left+dp[j]
                    left = dp[j]
        return dp[-1]
             
# Tabulation
obj = Solution()
print(obj.uniquePaths(3,7))
        
        