import pygame
from simulation import draw_grid, create_grid
from path_planning import astar

pygame.init()

ROWS = 20

# FULLSCREEN MODE
win = pygame.display.set_mode((800, 800))
WIDTH = win.get_width()
HEIGHT = win.get_height()

pygame.display.set_caption("Autonomous Navigation 🤖")

grid = create_grid()

start = None
end = None
path = []

current_pos = None
step_index = 0

# Emoji font
try:
    font = pygame.font.SysFont("Segoe UI Emoji", 30)
except:
    font = pygame.font.SysFont("Arial", 30)

robot_emoji = font.render("🤖", True, (0, 0, 0))


def get_clicked_pos(pos):
    gap = min(WIDTH, HEIGHT) // ROWS

    # Center offset
    offset_x = (WIDTH - gap * ROWS) // 2
    offset_y = (HEIGHT - gap * ROWS) // 2

    x, y = pos

    # Adjust click to grid position
    col = (x - offset_x) // gap
    row = (y - offset_y) // gap

    return (row, col)


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # KEY CONTROLS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            # RESET (R key)
            if event.key == pygame.K_r:
                start = None
                end = None
                path = []
                current_pos = None
                step_index = 0

        # MOUSE CLICK (FIXED)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)

            # Ensure click inside grid
            if 0 <= row < ROWS and 0 <= col < ROWS:
                if not start:
                    start = (row, col)

                elif not end:
                    end = (row, col)
                    path = astar(grid, start, end)
                    current_pos = start
                    step_index = 0

    # MOVE ROBOT STEP-BY-STEP
    if path and step_index < len(path):
        current_pos = path[step_index]
        step_index += 1

    win.fill((255, 255, 255))

    # DRAW GRID
    draw_grid(win, grid, path, start, end, WIDTH, HEIGHT)

    # DRAW ROBOT 🤖
    if current_pos:
        gap = min(WIDTH, HEIGHT) // ROWS
        offset_x = (WIDTH - gap * ROWS) // 2
        offset_y = (HEIGHT - gap * ROWS) // 2

        win.blit(
            robot_emoji,
            (
                offset_x + current_pos[1] * gap,
                offset_y + current_pos[0] * gap,
            ),
        )

    pygame.display.update()

pygame.quit()