import pygame
import os
from animal import Animal

SHEEP_STRENGTH = 4
SHEEP_INITIATIVE = 4
SHEEP_IMAGE = pygame.image.load(os.path.join('assets', 'sheep.png'))

class Sheep(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, SHEEP_INITIATIVE, SHEEP_STRENGTH, SHEEP_IMAGE)