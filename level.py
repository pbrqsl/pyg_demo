import pygame
from settings import WORLD_MAP

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        print('setting up level')
        self.create_map()

    def create_map(self):
        for row in WORLD_MAP:
            print(row)

    def run(self):
        pass