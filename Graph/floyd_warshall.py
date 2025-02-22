def floyd_warshall_with_path(graph):
    INF = float('inf')
    nodes = list(graph.keys())
    n = len(nodes)

    # Initialize distance and parent matrices
    dist = {i: {j: INF for j in nodes} for i in nodes}
    parent = {i: {j: None for j in nodes} for i in nodes}

    # Set initial distances
    for u in graph:
        dist[u][u] = 0
        for v, w in graph[u]:
            dist[u][v] = w
            parent[u][v] = u  # Store the predecessor

    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]  # Update path

    # Detect negative cycles
    for i in nodes:
        if dist[i][i] < 0:
            return "Negative cycle detected"

    return dist, parent

# Path reconstruction function
def reconstruct_path(parent, start, end):
    if parent[start][end] is None:
        return "No path"
    
    path = []
    while end is not None:
        path.append(end)
        end = parent[start][end]
    
    path.reverse()
    return path

# Example usage:
graph = {
    1: [(2, 3)],
    2: [(3, -2)],
    3: [(4, 2)],
    4: [(2, 1)]
}

dist, parent = floyd_warshall_with_path(graph)
if dist != "Negative cycle detected":
    print("Shortest Distance Matrix:")
    for u in dist:
        print(f"{u}: {dist[u]}")
    
    print("\nPath from 1 to 4:", reconstruct_path(parent, 1, 4))
else:
    print(dist)
