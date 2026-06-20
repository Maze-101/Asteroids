import pygame
import sys
from pygame import *
from pygame.sprite import Group
from pygame.time import Clock
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import *
from asteroid import *
from asteroidfeild import *
from shot import *
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen : Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock : Clock = pygame.time.Clock()
    dt : float = 0.0
    updatable : Group = pygame.sprite.Group()
    drawable : Group = pygame.sprite.Group()
    asteroids : Group = pygame.sprite.Group()
    shots : Group = pygame.sprite.Group()
    Shot.containers = (updatable,drawable,shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = updatable
    player : Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field : AsteroidField = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        player.update(dt)
        player.shoot_cooldown -= dt
        for asteroid in asteroids:
            if player.collide_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collide_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        display.flip()
        dt = clock.tick(90) / 1000

if __name__ == "__main__":
    main()
