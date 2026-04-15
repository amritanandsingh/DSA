from typing import List

class Solution:
    
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [[-189 for _ in range(len(triangle))] for _ in range(len(triangle))] 
        dp[0][0] = triangle[0][0]
        for i in range(1 , len(triangle)):
            
            for j in range(len(triangle[i])):
                
                # just above
                justAbove = float('inf')
                if dp[i-1][j] != -189:
                    justAbove = triangle[i][j] + dp[i-1][j]
                # just above left
                justAboveLeft = float('inf')
                if dp[i-1][j-1] != -189:
                    justAboveLeft = triangle[i][j] + dp[i-1][j-1]
                dp[i][j] = min(justAbove , justAboveLeft)
        ans = float('inf')
        for i in range(len(dp)):
            ans=min(ans , dp[-1][i])
        return ans
