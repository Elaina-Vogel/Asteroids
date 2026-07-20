import pygame
import player
import asteroid
import shot
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initilize game
    pygame.init()

    # init clock
    clock = pygame.time.Clock()
    dt = 0.0

    # init groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, drawable, updatable)

    # init player
    p = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # init asteroids
    af = AsteroidField()

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

        for u in updatable:
            u.update(dt)

        # check for bullet asteroid collisions
        for a in asteroids:
            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    a.kill()
                    s.kill()

        # check for asteroid player collisions
        for a in asteroids:
            if a.collides_with(p):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        #print(f"updated dt: {dt}")


if __name__ == "__main__":
    main()
