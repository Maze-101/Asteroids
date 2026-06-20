import pygame
from pygame import * # type: ignore
from pygame.time import Clock
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen : Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock : Clock = pygame.time.Clock()
    dt : float = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
