# work for undirected graphs only !
import heapq


def prims_algorithm(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start, -1)]  # (weight, current_node, parent_node)
    mst_edges = []  # Store edges of MST
    total_cost = 0
    path_dict = {i: [] for i in range(n)}  # Store node-to-next-nodes mapping

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += weight

        if parent != -1:
            mst_edges.append((parent, u, weight))
            path_dict[parent].append(u)
            path_dict[u].append(parent)

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst_edges, total_cost, path_dict


# Example usage
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

mst, cost, path_dict = prims_algorithm(graph, start=0)
print("Minimum Spanning Tree edges:")
for u, v, w in mst:
    print(f"{u} - {v} (weight {w})")
print(f"Total Cost: {cost}")
print("Path Dictionary:")
print(path_dict)
