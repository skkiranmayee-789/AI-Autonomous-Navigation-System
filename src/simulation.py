import pygame

WIDTH = 600
ROWS = 20

import pygame

ROWS = 20

def draw_grid(win, grid, path, start, end, width, height):
    gap = min(width, height) // ROWS

    # center grid
    offset_x = (width - gap * ROWS) // 2
    offset_y = (height - gap * ROWS) // 2

    for i in range(ROWS):
        for j in range(ROWS):
            color = (255, 255, 255)

            if grid[i][j] == 1:
                color = (0, 0, 0)

            if (i, j) in path:
                color = (0, 255, 0)

            if (i, j) == start:
                color = (0, 0, 255)

            if (i, j) == end:
                color = (255, 0, 0)

            pygame.draw.rect(
                win,
                color,
                (offset_x + j * gap, offset_y + i * gap, gap, gap)
            )

    # grid lines
    for i in range(ROWS):
        pygame.draw.line(win, (200, 200, 200),
                         (offset_x, offset_y + i * gap),
                         (offset_x + ROWS * gap, offset_y + i * gap))

        pygame.draw.line(win, (200, 200, 200),
                         (offset_x + i * gap, offset_y),
                         (offset_x + i * gap, offset_y + ROWS * gap))

def create_grid():
    grid = [[0]*20 for _ in range(20)]

    # Vertical buildings (leave gaps as roads)
    for col in range(3, 17, 4):
        for row in range(20):
            if row not in [5, 10, 15]:  # roads
                grid[row][col] = 1

    # Horizontal buildings
    for row in range(4, 18, 4):
        for col in range(20):
            if col not in [2, 8, 14]:  # roads
                grid[row][col] = 1

    return grid