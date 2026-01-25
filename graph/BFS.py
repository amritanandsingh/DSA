from collections import deque


class Solution:
    def bfsOfGraph(self, V, adj):
        ans=[]
        my_queue = deque()
        visited = [0]* (V+1)
        my_queue.append(0)
        visited[0] = 1
        while len(my_queue) != 0:
            temp = my_queue.popleft()    
            ans.append(temp)
            for i in adj[temp]:
                if visited[i] == 0:
                    my_queue.append(i)
                    visited[i] = 1
        return ans

obj = Solution();
v=5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
ans = obj.bfsOfGraph(v, adj)
print(ans)
# ============================================================================

