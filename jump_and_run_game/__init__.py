from jump_and_run_game._version import __version__
from os import environ
import sys

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

__all__ = [
    "__version__",
]

import pygame  # noqa: E402


# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Player:
    JUMP_HEIGHT = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.jump_count = Player.JUMP_HEIGHT
        self.is_jumping = False
        self.width = 50
        self.height = 50

    def move_left(self) -> None:
        self.x -= self.speed

    def move_right(self) -> None:
        self.x += self.speed

    def jump(self) -> None:
        if not self.is_jumping:
            self.is_jumping = True

    def update(self) -> None:
        if self.is_jumping:
            if self.jump_count >= -Player.JUMP_HEIGHT:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count**2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = Player.JUMP_HEIGHT

    def render(self, screen: pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))


def handle_user_input(keys: pygame.key.ScancodeWrapper, player: Player) -> None:
    if keys[pygame.K_LEFT] and player.x > 0:
        player.move_left()
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 50:
        player.move_right()
    if keys[pygame.K_SPACE]:
        player.jump()


def core_game_loop(
    screen: pygame.surface.Surface, clock: pygame.time.Clock, player: Player
) -> None:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input
    keys = pygame.key.get_pressed()
    handle_user_input(keys, player)

    # Update game state
    player.update()

    # Render graphics
    screen.fill(WHITE)
    player.render(screen)

    pygame.display.flip()
    clock.tick(FPS)


def main():
    pygame.init()

    # Setup the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jump and Run Game")

    # Create core objects
    clock = pygame.time.Clock()
    player = Player(50, HEIGHT - 100)

    while True:
        core_game_loop(screen, clock, player)


if __name__ == "__main__":
    main()
