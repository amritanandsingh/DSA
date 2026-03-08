
class Solution:
    def fun(self, obstacleGrid,i,j):
        if i>=0 and j>=0 and obstacleGrid[i][j] == 1:
            return 0
        if i<0 or j<0:
            return 0
        
        if 0 == i or 0 == j :
            return 1
        
        top = self.fun(obstacleGrid,i-1,j)
        left = self.fun(obstacleGrid,i,j-1)
        return left+top

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
       
        return self.fun(obstacleGrid ,len(obstacleGrid)-1 , len(obstacleGrid[0]) -1 )
        
sol = Solution()
print(sol.uniquePathsWithObstacles([[0,1,0,0]]))
#print(sol.uniquePathsWithObstacles([[0,0]]))
#print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))
#print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
