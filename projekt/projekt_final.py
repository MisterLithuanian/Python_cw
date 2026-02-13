
import pygame
import sys
import time
import random 

WIDTH, HEIGHT = 1000, 600
CELL_SIZE = 40
MARGIN = 2
FPS = 30

weight = [2, 3, 4, 5] 
capacity = 8
n = len(weight)
profit = []

ROWS = n + 1
COLS = capacity + 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
GREEN = (144, 238, 144)
YELLOW = (255, 255, 153)
RED = (255, 100, 100)  

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Problem plecakowy")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 32)
dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]


def randomize_data():
    global profit, dp
    profit = [random.randint(1, 10) for _ in range(n)]
    
    dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    print(f"Nowe wylosowane wartości: {profit}")


def draw_text(text, x, y, color=BLACK, fnt=font):
    img = fnt.render(text, True, color)
    screen.blit(img, (x, y))


def draw_table(highlight=None):
    screen.fill(WHITE)

    for c in range(COLS):
        draw_text(str(c), 100 + c * CELL_SIZE + 10, 50)

    for r in range(ROWS):
        if r == 0:
            label = "0"
        else:
            label = f"w={weight[r-1]}, v={profit[r-1]}"
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

    draw_text("Problem plecakowy ", 100, 10, fnt=big_font)
    pygame.display.flip()


def knapsack():
    for i in range(1, ROWS):
        for w in range(COLS):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if weight[i - 1] <= w:
                val_without = dp[i - 1][w]
                val_with = dp[i - 1][w - weight[i - 1]] + profit[i - 1]
                dp[i][w] = max(val_without, val_with)
            else:
                dp[i][w] = dp[i - 1][w]

            draw_table(highlight=(i, w))
            time.sleep(0.2) 


start_button = pygame.Rect(800, 500, 150, 50)
reset_button = pygame.Rect(600, 500, 150, 50)

started = False 

randomize_data()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos) and not started:
                started = True
                knapsack()
            
            if reset_button.collidepoint(event.pos):
                started = False 
                randomize_data() 

    screen.fill(WHITE)
    draw_table()

    color_start = GREEN if not started else GRAY
    pygame.draw.rect(screen, color_start, start_button, border_radius=8)
    pygame.draw.rect(screen, BLACK, start_button, 2, border_radius=8)
    draw_text("START", start_button.x + 45, start_button.y + 15)

    pygame.draw.rect(screen, RED, reset_button, border_radius=8)
    pygame.draw.rect(screen, BLACK, reset_button, 2, border_radius=8)
    draw_text("LOSUJ", reset_button.x + 10, reset_button.y + 15)

    pygame.display.flip()
    clock.tick(FPS)