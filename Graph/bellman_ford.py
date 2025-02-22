def bellman_ford(n, edges, src, dest):
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n  # Track the path
    dist[src] = 0

    # Relax all edges (n-1) times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u  # Store predecessor

    # Check for negative cycles (optional)
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return "Negative cycle detected"

    # Path reconstruction
    path = []
    node = dest
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()

    return dist[dest], path if dist[dest] != INF else "No path"

# Example: Graph with 5 nodes, edges in (u, v, weight) format
edges = [(0, 1, 4), (0, 2, 2), (1, 2, 3), (1, 3, 2), (2, 3, 5), (3, 4, 1)]
print(bellman_ford(5, edges, 0, 4))  # Output: (Shortest Distance, Path)
