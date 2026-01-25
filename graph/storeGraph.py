"""
Graph Representation Tutorial - Storing Graphs in Different Ways
==================================================================

A GRAPH is a non-linear data structure consisting of:
- VERTICES (Nodes): Entities/Points in the graph
- EDGES: Connections between vertices

Video explains 3 main ways to represent/store a graph:
1. Adjacency Matrix
2. Adjacency List
3. Edge List
"""

# ============================================================================
# METHOD 1: ADJACENCY MATRIX (2D Array Representation)
# ============================================================================
"""
Use a 2D matrix where:
- matrix[i][j] = 1 if edge exists between vertex i and j
- matrix[i][j] = 0 if no edge

Best for: Dense graphs (many edges)
Time: O(1) to check if edge exists
Space: O(V²) - wasteful for sparse graphs
"""

class GraphAdjacencyMatrix:
    def __init__(self, vertices):
        self.V = vertices
        # Create V x V matrix filled with 0s
        self.matrix = [[0] * vertices for _ in range(vertices)]
    
    def addEdge(self, u, v, weight=1):
        """Add an edge between vertices u and v"""
        self.matrix[u][v] = weight
        # Uncomment for undirected graph:
        # self.matrix[v][u] = weight
    
    def printMatrix(self):
        """Print the adjacency matrix"""
        for row in self.matrix:
            print(row)

# Example:
# Graph with 5 vertices
graph1 = GraphAdjacencyMatrix(5)
graph1.addEdge(0, 1)  # Edge from 0 to 1
graph1.addEdge(0, 4)
graph1.addEdge(1, 2)
graph1.addEdge(2, 3)
print("Adjacency Matrix:")
graph1.printMatrix()


# ============================================================================
# METHOD 2: ADJACENCY LIST (Dictionary/Array of Lists Representation)
# ============================================================================
"""
Use a dictionary/array where each vertex maps to a list of its neighbors

Best for: Sparse graphs (few edges), most practical
Time: O(V + E) for most operations
Space: O(V + E) - efficient
"""

class GraphAdjacencyList:
    def __init__(self, vertices):
        self.V = vertices
        # Create adjacency list as dictionary
        self.graph = {i: [] for i in range(vertices)}
    
    def addEdge(self, u, v, weight=1):
        """Add an edge from u to v"""
        self.graph[u].append((v, weight))
        # Uncomment for undirected graph:
        # self.graph[v].append((u, weight))
    
    def printGraph(self):
        """Print the adjacency list"""
        for vertex, neighbors in self.graph.items():
            print(f"Vertex {vertex}: {neighbors}")
    
    def getNeighbors(self, vertex):
        """Get all neighbors of a vertex"""
        return self.graph[vertex]

# Example:
graph2 = GraphAdjacencyList(5)
graph2.addEdge(0, 1)
graph2.addEdge(0, 4)
graph2.addEdge(1, 2)
graph2.addEdge(2, 3)
print("\nAdjacency List:")
graph2.printGraph()


# ============================================================================
# METHOD 3: EDGE LIST (List of All Edges)
# ============================================================================
"""
Store all edges as a list of (source, destination, weight) tuples

Best for: Algorithms like Kruskal's (needs to process all edges)
Time: O(E) to iterate through all edges
Space: O(E)
"""

class GraphEdgeList:
    def __init__(self):
        self.edges = []  # List of (u, v, weight) tuples
        self.vertices = set()
    
    def addEdge(self, u, v, weight=1):
        """Add an edge"""
        self.edges.append((u, v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
    
    def printEdges(self):
        """Print all edges"""
        for u, v, weight in self.edges:
            print(f"({u} -> {v}, weight: {weight})")
    
    def getEdges(self):
        """Return all edges sorted by weight (useful for MST algorithms)"""
        return sorted(self.edges, key=lambda x: x[2])

# Example:
graph3 = GraphEdgeList()
graph3.addEdge(0, 1, 5)
graph3.addEdge(0, 4, 2)
graph3.addEdge(1, 2, 3)
graph3.addEdge(2, 3, 7)
print("\nEdge List:")
graph3.printEdges()


# ============================================================================
# COMPARISON & WHEN TO USE
# ============================================================================
"""
┌─────────────┬──────────────┬──────────────┬─────────────────┐
│ Operation   │ Adj. Matrix  │ Adj. List    │ Edge List       │
├─────────────┼──────────────┼──────────────┼─────────────────┤
│ Check Edge  │ O(1)         │ O(degree)    │ O(E)            │
│ Add Edge    │ O(1)         │ O(1)         │ O(1)            │
│ Remove Edge │ O(1)         │ O(degree)    │ O(E)            │
│ Space       │ O(V²)        │ O(V+E)       │ O(E)            │
│ Dense Graph │ Good         │ Bad          │ Bad             │
│ Sparse Graph│ Bad          │ Good         │ Good            │
└─────────────┴──────────────┴──────────────┴─────────────────┘

Use Adjacency List for most interview/practical problems!
"""

# ============================================================================
# PRACTICAL EXAMPLE: Build Same Graph in All 3 Ways
# ============================================================================

print("\n" + "="*50)
print("Building a graph: 0->1, 0->2, 1->2, 2->0, 2->3")
print("="*50)

# Method 1: Adjacency Matrix
print("\n1. ADJACENCY MATRIX:")
adj_matrix = [
    [0, 1, 1, 0],  # 0 connects to 1, 2
    [0, 0, 1, 0],  # 1 connects to 2
    [1, 0, 0, 1],  # 2 connects to 0, 3
    [0, 0, 0, 0]   # 3 has no outgoing edges
]
for i, row in enumerate(adj_matrix):
    print(f"Vertex {i}: {row}")

# Method 2: Adjacency List (Most Common)
print("\n2. ADJACENCY LIST:")
adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: []
}
for vertex, neighbors in adj_list.items():
    print(f"Vertex {vertex}: {neighbors}")

# Method 3: Edge List
print("\n3. EDGE LIST:")
edge_list = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 0),
    (2, 3)
]
for u, v in edge_list:
    print(f"({u} -> {v})")
