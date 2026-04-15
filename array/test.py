from typing import List
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # Creates a 3x4 matrix filled with zeros
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tempRow = (0 if i==0 else matrix[i-1][j])
                tempCol =  (0 if j== 0 else matrix[i][j-1])
                matrix[i][j] = tempRow + tempCol + grid[i][j] 
        print(matrix)




obj = Solution()
obj.countSubmatrices([[7,6,3],[6,6,1]], 18)