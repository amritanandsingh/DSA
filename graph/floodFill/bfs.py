import collections
from collections import deque
from typing import List

import collections
from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        q=deque()
        q.append([sr,sc])
        # soringing the orignal color and assigning new color if pixel is same as orignal color
        orignalColor = image[sr][sc]
        image[sr][sc] = color
        visited[sr][sc] = 1
        
        while len(q)!=0:
            temp=q.popleft()
            lRow = [0,0,-1,1]
            lCol = [-1,1,0,0]
            for i in range(4):
                newRow= temp[0] + lRow[i]
                newCol = temp[1] + lCol[i]
                if  newRow>=0 and newCol>=0 and  newRow < len(image) and newCol < len(image[0])  and visited[newRow][newCol] == 0 and image[newRow][newCol] == orignalColor:
                    q.append([newRow,newCol])
                    image[newRow][newCol] = color
                    visited[newRow][newCol] = 1
        return image



        

object=Solution()
print(object.floodFill([[0,0,0],[0,0,0]],1,0,2))
