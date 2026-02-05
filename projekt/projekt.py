import pygame
import sys
import time

WIDTH, HEIGHT = 1000, 600  # Wymiary okna
CELL_SIZE = 40             # Rozmiar pojedynczej komórki w tabeli (piksele)
MARGIN = 2                 # Odstęp między komórkami
FPS = 30                   # Klatki na sekundę (szybkość odświeżania okna)


weight = [2, 3, 4, 5] # Wagi przedmiotów
profit = [3, 4, 5, 8] # Wartości przedmiotów
capacity = 8 # Maksymalna pojemność plecaka
n = len(weight) # Liczba przedmiotów

ROWS = n + 1 # Wiersze 
COLS = capacity + 1 # Kolumny 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)      
GREEN = (144, 238, 144)    
YELLOW = (255, 255, 153)   

# INICJALIZACJA PYGAME
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Problem plecakowy - Wizualizacja")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 32)

# Inicjalizacja tablicy zerami.
dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]


def draw_text(text, x, y, color=BLACK, fnt=font):
    # Rysuje tekst na ekranie w podanej pozycji
    img = fnt.render(text, True, color)
    screen.blit(img, (x, y))


def draw_table(highlight=None):
    # Rysuje całą tabelę , nagłówki oraz aktualny stan obliczeń
    screen.fill(WHITE) 
    #  Rysowanie nagłówków kolumn (pojemności plecaka 8)
    for c in range(COLS):
        draw_text(str(c), 100 + c * CELL_SIZE + 10, 50)

    # Rysowanie nagłówków wierszy 
    for r in range(ROWS):
        label = "0" if r == 0 else f"w={weight[r-1]}, v={profit[r-1]}"
        draw_text(label, 10, 100 + r * CELL_SIZE + 10)

    # Rysowanie siatki i wartości w komórkach
    for r in range(ROWS):
        for c in range(COLS):
            # Obliczanie pozycji x, y dla danej komórki
            x = 100 + c * CELL_SIZE
            y = 100 + r * CELL_SIZE
            
            color = GRAY

            if highlight == (r, c):
                color = YELLOW

            # Rysowanie kwadratu 
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN))
            # Rysowanie obramowania 
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN), 1)

            draw_text(str(dp[r][c]), x + 10, y + 10) # Wypisanie wartości liczbowej wewnątrz komórki

    # Tytuł na górze
    draw_text("Problem plecakowy ", 100, 10, fnt=big_font)
    
    # Odświeżenie ekranu
    pygame.display.flip()


def knapsack():
    # Pętla po przedmiotach (od 1 do n)
    for i in range(1, ROWS):
        # Pętla po pojemnościach plecaka (od 0 do capacity)
        for w in range(COLS):
            
            # Obsługa zdarzeń wewnątrz pętli 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Sprawdzenie, czy waga aktualnego przedmiotu mieści się w aktualnej pojemności 'w'
            if weight[i - 1] <= w:
                # Wybieramy maksimum z dwóch opcji:
                # 1. Nie bierzemy przedmiotu (wartość z wiersza wyżej: dp[i-1][w])
                # 2. Bierzemy przedmiot (wartość tego przedmiotu + najlepszy wynik dla pozostałej pojemności)
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weight[i - 1]] + profit[i - 1]
                )
            else:
                # Przedmiot się nie mieści, przepisujemy wynik z wiersza wyżej
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