import pygame
import sys
import time

WIDTH, HEIGHT = 1000, 600
CELL_SIZE = 40
MARGIN = 2
FPS = 30

weight = [2, 3, 4, 5]
profit = [3, 4, 5, 8]
capacity = 8
n = len(weight)

ROWS = n + 1
COLS = capacity + 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
GREEN = (144, 238, 144)
YELLOW = (255, 255, 153)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Problem plecakowy")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 32)

dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_text(text, x, y, color=BLACK, fnt=font):
    img = fnt.render(text, True, color)
    screen.blit(img, (x, y))


def draw_table(highlight=None):
    screen.fill(WHITE)

    for c in range(COLS):
        draw_text(str(c), 100 + c * CELL_SIZE + 10, 50)

    for r in range(ROWS):
        label = "0" if r == 0 else f"w={weight[r-1]}, v={profit[r-1]}"
        draw_text(label, 10, 100 + r * CELL_SIZE + 10)

    for r in range(ROWS):
        for c in range(COLS):
            x = 100 + c * CELL_SIZE
            y = 100 + r * CELL_SIZE
            color = GRAY

            if highlight == (r, c):
                color = YELLOW

            pygame.draw.rect(screen, color, (x, y, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN))
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN), 1)

            draw_text(str(dp[r][c]), x + 10, y + 10)

    draw_text("Problem plecakowy", 100, 10, fnt=big_font)
    pygame.display.flip()

def knapsack():
    for i in range(1, ROWS):
        for w in range(COLS):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if weight[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weight[i - 1]] + profit[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

            draw_table(highlight=(i, w))
            time.sleep(0.4)


button_rect = pygame.Rect(800, 500, 150, 50)
started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not started:
            if button_rect.collidepoint(event.pos):
                started = True
                knapsack()

    screen.fill(WHITE)
    draw_table()

    color = GREEN if not started else GRAY
    pygame.draw.rect(screen, color, button_rect, border_radius=8)
    pygame.draw.rect(screen, BLACK, button_rect, 2, border_radius=8)
    draw_text("START", button_rect.x + 45, button_rect.y + 15)

    pygame.display.flip()
    clock.tick(FPS)
