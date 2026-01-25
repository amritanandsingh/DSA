class Solution:
    def dfsHealper(self,i,adj,visited,ans):
        visited[i]=1
        ans.append(i)
        for j in adj[i]:
            if visited[j]==0:
                self.dfsHealper(j,adj,visited,ans)

    def dfs(self, adj):
        visited = [0] * len(adj)
        ans=[]
        for i in range(0,len(adj)):
            if visited[i]==0:
                self.dfsHealper(i,adj,visited,ans)
        return ans
        # code here


obj=Solution()
adj= [[2, 3, 1], [0], [0, 4], [0], [2]]
ans=obj.dfs(adj)
print(ans)