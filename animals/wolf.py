import pygame
import os
from animal import Animal

WOLF_STRENGTH = 9
WOLF_INITIATIVE = 5
WOLF_IMAGE = pygame.image.load(os.path.join('assets', 'wolf.png'))

class Wolf(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, WOLF_INITIATIVE, WOLF_STRENGTH, WOLF_IMAGE)