import pygame
from assets import GAME_ASSETS

class GameDone():
    def __init__(self, window):
        self.window = window
        self.gamedone = pygame.image.load('game_end.png')
        self.scaled_gamedone = pygame.transform.scale(self.gamedone, (600, 600))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.blit(self.scaled_gamedone, (600, 600))
            pygame.display.flip()