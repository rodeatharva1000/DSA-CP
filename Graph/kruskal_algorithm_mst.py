# work only for undirected graph !
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Parent array
        self.rank = [0] * n  # Rank array for union by rank

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's Algorithm
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(n)
    mst_dict = {i: [] for i in range(n)}  # Minimum Spanning Tree as adjacency list
    mst_list = []  # Minimum Spanning Tree as edge list
    
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):  # Check if adding the edge forms a cycle
            ds.union(u, v)
            mst_dict[u].append((v, weight))
            mst_dict[v].append((u, weight))
            mst_list.append((u, v, weight))
        
        if len(mst_list) == n - 1:  # Stop when we have (V-1) edges
            break
    
    return mst_dict, mst_list

# Example Usage (Graph with 6 nodes labeled 0 to 5)
n = 6  # Number of vertices
edges = [  # (node1, node2, weight)
    (0, 1, 1), (1, 3, 2), (2, 3, 3), (1, 2, 4), (0, 2, 5), 
    (2, 4, 6), (3, 4, 7), (3, 5, 8), (4, 5, 9)
]

mst_dict, mst_list = kruskal(n, edges)
print("Minimum Spanning Tree (Adjacency List):")
for node, neighbors in mst_dict.items():
    print(f"{node}: {neighbors}")

print("\nMinimum Spanning Tree (Edge List):")
for u, v, weight in mst_list:
    print(f"{u} - {v} : {weight}")
