import pygame
from constants import *

def main():
    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        color = pygame.Color(0, 0, 0,)
        pygame.display.flip()
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH} ")
        print(f"Screen height: {SCREEN_HEIGHT} ")









if __name__ == "__main__":
    main()