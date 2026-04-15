import sys
sys.setrecursionlimit(10**6)
from typing import List

class Solution:
    def fun(self , col , row , grid , sumTillNow , dp):
        if col < 0 or row < 0:
            return float("inf")
        if col==0 and row == 0:
            return grid[0][0]+sumTillNow
        
        # if dp[col][row] != 0:
        #     return dp[row][col]
        

        sumTillNow += grid[col][row]
        left = self.fun(col-1 , row , grid , sumTillNow , dp)
        top = self.fun(col, row-1 , grid , sumTillNow , dp)
        #dp[col][row]=min(left , top)
        return  min(left , top) #dp[col][row]

    def minPathSum(self, grid: List[List[int]]) -> int:
        col = len(grid)
        row = len(grid[0])
        dp=[]
        rowOfDp = row*[0]
        for i in range(col):
            dp.append(rowOfDp)
        return self.fun(col-1 , row-1 , grid , 0,dp)
    
obj = Solution()
print(obj.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]))