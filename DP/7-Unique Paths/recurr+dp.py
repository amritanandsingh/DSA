class Solution:
    def fun(self ,i,j ,dp):
        if(dp[i][j] != 0):
            return dp[i][j]
        if i == 0 and j== 0:
            return 1
        if i < 0 or j < 0:
            return 0
        left = self.fun(i,j-1,dp)
        up =  self.fun(i-1,j,dp)
        dp[i][j] = left + up
        return dp[i][j]
        

    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        print(dp)
        return self.fun(m-1,n-1 , dp)
        

# class Solution:
obj = Solution()
print(obj.uniquePaths(3,7))