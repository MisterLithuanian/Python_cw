import pygame
import random
import sys

WIDTH, HEIGHT = 1000, 1000
FPS = 60
SNOW_RADIUS = 10
SNOW_SPEED = 2
SPAWN_INTERVAL = 1000  

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Snowflake:
    def __init__(self):
        self.x = random.randint(SNOW_RADIUS, WIDTH - SNOW_RADIUS)
        self.y = -SNOW_RADIUS
        self.radius = SNOW_RADIUS
        self.speed = SNOW_SPEED

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        mx, my = pos
        return (self.x - mx) ** 2 + (self.y - my) ** 2 <= self.radius ** 2


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Padający śnieg")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)

    snowflakes = []
    score = 0
    game_over = False

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_INTERVAL)

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.type == SPAWN_EVENT:
                    snowflakes.append(Snowflake())

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for flake in snowflakes[:]:
                        if flake.is_clicked(event.pos):
                            snowflakes.remove(flake)
                            score += 1
                            break

        if not game_over:
            for flake in snowflakes:
                flake.update()
                if flake.y - flake.radius >= HEIGHT:
                    game_over = True

        screen.fill(BLACK)

        for flake in snowflakes:
            flake.draw(screen)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if game_over:
            text = font.render("GAME OVER", True, WHITE)
            screen.blit(
                text,
                (WIDTH // 2 - text.get_width() // 2,
                 HEIGHT // 2 - text.get_height() // 2)
            )

        pygame.display.flip()


if __name__ == "__main__":
    main()
