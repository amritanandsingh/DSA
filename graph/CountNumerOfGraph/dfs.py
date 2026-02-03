from typing import List

class Solution:
    def dfsHelper(self, itr ,isConnected , visited):
        visited[itr]=1
        for i in range(len(isConnected)):
            if isConnected[itr][i]==1 and visited[i]==0 and itr!= i:
                self.dfsHelper(i,isConnected , visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*len(isConnected)
        ans=0
        for i in range(len(isConnected)):
            if visited[i]==0:
                self.dfsHelper( i,isConnected,visited)
                ans+=1
        return ans


obj = Solution()
print(obj.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Output: 2
