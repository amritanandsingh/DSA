from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited= [[0]*len(grid[0]) for _ in range(len(grid))]
        maxTime=0
        q=deque()
        # put all rotten oranges in queue
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    visited[i][j]=1
                    q.append([i,j,0])
        while len(q) != 0:
            tempQ = q.popleft()
            rottenRow=tempQ[0]
            rottenCol = tempQ[1]
            time = tempQ[2]
            # four directions if any fresh orange is there
            toItrRow=[0,0,1,-1]
            toItrCol=[1,-1,0,0]
            for i in range(4):
                newRow=toItrRow[i] + rottenRow
                newCol=toItrCol[i]+rottenCol
                if newRow<len(grid) and newCol<len(grid[0]) and newRow>=0 and newCol>=0   and visited[newRow][newCol] == 0 and grid[newRow][newCol] == 1:
                    visited[newRow][newCol] = 1
                    q.append([newRow,newCol,time+1])
                    maxTime= max(time+1,maxTime)
        for i in range(len(visited)):
            for j in range(len(visited[i])):
                if grid[i][j] == 1 and visited[i][j] == 0:  ## if there is any fresh orange left
                    return -1

        return maxTime

obj=Solution()
print(obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Expected output: 4
print(obj.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # Expected output: -1
print(obj.orangesRotting([[0,2]]))              # Expected output: 0