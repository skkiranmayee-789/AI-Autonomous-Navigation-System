import heapq

def astar(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        neighbors = [(0,1),(1,0),(-1,0),(0,-1)]

        for dx, dy in neighbors:
            neighbor = (current[0]+dx, current[1]+dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                temp_g = g_score[current] + 1

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f, neighbor))
                    came_from[neighbor] = current

    return []