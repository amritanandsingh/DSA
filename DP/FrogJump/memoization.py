class Solution:
    def fun(self , height, idx, dp  ):
        if dp[idx] != -1:
            return dp[idx]
        if idx == 0:
            return 0
        left = self.fun(height, idx-1 , dp ,) + abs(height[idx] - height[idx-1]  ) 
        right = float("inf") 
        if idx > 1:
            right = self.fun( height, idx-2 , dp) + abs(height[idx] - height[idx-2] ) 
        dp[idx] = min(left,right)
        return min(left,right)
    def minCost(self, height):
        dp=[-1] * len(height)
        return self.fun(height , (len(height)-1) , dp  )
        # code here