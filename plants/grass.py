import pygame
import os
from plant import Plant

GRASS_STRENGTH = 0
GRASS_IMAGE = pygame.image.load(os.path.join('assets', 'grass.png'))

class Grass(Plant):
    def __init__(self, world, position):
        super().__init__(world, position, GRASS_STRENGTH, GRASS_IMAGE)