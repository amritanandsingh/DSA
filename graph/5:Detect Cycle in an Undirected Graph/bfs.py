# https://takeuforward.org/plus/dsa/problems/detect-a-cycle-in-an-undirected-graph
'''
Core Idea : keep tracking the who is the parent of the current node, if we encounter a visited node which is not the parent of the current node, then there is a cycle in the graph.
'''
from collections import deque


class Solution:
    def bfs(self, edges, visited, idx):
        q = deque()
        q.append([-1, idx])
        while len(q) > 0:
            payload = q.popleft()
            paraent = payload[0]
            currectNode = payload[1]
            visited[currectNode] = True
            for i in edges[currectNode]:
                if visited[i] == False:
                    q.append([currectNode, i])
                elif paraent != -1 and i != paraent:
                    return True
        return False

    def isCycle(self, V, edges):
        visited = [False] * V

        # BUG: You are passing an EDGE LIST (e.g., [[0,1],[0,2],...]),
        #      but bfs() expects an ADJACENCY LIST (edges[u] = [neighbors...]).
        # FIX: Convert edge-list -> adjacency-list.
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BUG: iterating `range(len(edges))` is wrong when edges is an edge-list (len = E, not V).
        # FIX: iterate over vertices.
        for i in range(V):
            if visited[i] == False:
                if self.bfs(adj, visited, i) == True:
                    return True
        return False


        # Code here

obj = Solution()
print(obj.isCycle(4,  [[0, 1], [0, 2], [1, 2], [2, 3]]))
print(obj.isCycle(4,  [[0, 1], [1, 2], [2, 3]]))

# note : takeaway adjaceny list vs edge list