import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = (drawable, updatable) # type: ignore

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    print("Starting Asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('closing time')
                return

        updatable.update(dt)

        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

if __name__ == '__main__':
    main()
