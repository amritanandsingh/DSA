from typing import List

class Solution:
    def fun(self, triangle , m , n , dp):
        if dp[m][n] != -1:
            return dp[m][n]
        if m==0 and n == 0:
            return triangle[0][0]
        if m < 0 or n < 0   :
            return float("inf")

        justAbove = float("inf")
        if len(triangle[m]) > n and len(triangle[m-1]) > n:
            justAbove = self.fun(triangle , m-1 , n , dp ) 
        justAboveOfLeft = self.fun(triangle , m-1 , n-1 , dp )
        ans = min(justAbove , justAboveOfLeft) + triangle[m][n]
        dp[m][n] = ans
        return ans
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = float('inf')
        dp = [[-1 for _ in range(len(triangle))] for _ in range(len(triangle))] 
        for i in range(len(triangle)):
            t = self.fun(triangle,len(triangle) -1 , i , dp)
            ans = min(ans , t)

        return ans

