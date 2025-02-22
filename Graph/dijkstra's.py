import heapq

def dijkstra(n, edges, src, dst):
    graph, dist, parent = {i: [] for i in range(1, n + 1)}, {i: float('inf') for i in range(1, n + 1)}, {}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    pq, dist[src] = [(0, src)], 0
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]: continue
        for nei, w in graph[node]:
            if (nd := dist[node] + w) < dist[nei]:
                dist[nei], parent[nei] = nd, node
                heapq.heappush(pq, (nd, nei))
    
    path, cur = [], dst
    while cur in parent:
        path.append(cur)
        cur = parent[cur]
    return (dist[dst], path[::-1]) if dist[dst] != float('inf') else (float('inf'), [])

# Example usage
n, edges, src, dst = 5, [(1,2,2), (1,3,4), (2,3,1), (2,4,7), (3,5,3), (4,5,1)], 1, 5
print(dijkstra(n, edges, src, dst))
