import heapq


def astar_algorithm(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def heuristic(x, y): return abs(
        x - goal[0]) + abs(y - goal[1])  # Manhattan distance
    
    priority_queue = [(heuristic(*start), 0, start)]
    cost_map = {start: 0}
    parent_map = {start: None}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4-directional movement

    while priority_queue:
        _, current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:  # Goal reached, reconstruct path
            path, node = [], goal
            while node:
                path.append(node)
                node = parent_map[node]
            return path[::-1]  # Reverse to get correct order

        for dx, dy in directions:
            new_x, new_y = current_node[0] + dx, current_node[1] + dy
            # Valid move
            if 0 <= new_x < rows and 0 <= new_y < cols and not grid[new_x][new_y]:
                new_cost = current_cost + 1
                # Better path found
                if (new_x, new_y) not in cost_map or cost_map[(new_x, new_y)] > new_cost:
                    cost_map[(new_x, new_y)] = new_cost
                    parent_map[(new_x, new_y)] = current_node
                    heapq.heappush(
                        priority_queue, (new_cost + heuristic(new_x, new_y), new_cost, (new_x, new_y)))

    return None  # No path found


# Example grid (0 = open space, 1 = obstacle)
example_grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_position, goal_position = (0, 0), (4, 4)
shortest_path = astar_algorithm(example_grid, start_position, goal_position)
print("Shortest Path:", shortest_path)
