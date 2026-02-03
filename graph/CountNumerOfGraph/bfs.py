from collections import deque
from typing import List
class Solution:
    def bfsHelper(self, i, isConnected,visited):
        q=deque()
        q.append(i)
        visited[i]=1
        while len(q) != 0:
            temp = q.popleft()
            for j in range(len(isConnected[temp])):
                if j != temp and isConnected[temp][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    q.append(j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*len(isConnected)
        ans=0
        for i in range(len(isConnected)):
            if visited[i]==0:
                self.bfsHelper(i , isConnected,visited)
                ans+=1
        return ans


obj = Solution()
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
ans = obj.findCircleNum(isConnected)
print(ans)