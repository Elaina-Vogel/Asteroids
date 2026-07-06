import pygame
import player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initilize game
    pygame.init()

    # init clock
    clock = pygame.time.Clock()
    dt = 0.0

    # init player
    p = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # set new instance of GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # infinite loop for game loop
    while True:
        log_state()

        # start processing the pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        p.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        #print(f"updated dt: {dt}")


if __name__ == "__main__":
    main()
