import pygame
import os
from plant import Plant

DEADLY_NIGHTSHADE_STRENGTH = 99
DEADLY_NIGHTSHADE_IMAGE = pygame.image.load(os.path.join('assets', 'deadly_nightshade.png'))

class DeadlyNightshade(Plant):
    def __init__(self, world, position):
        super().__init__(world, position, DEADLY_NIGHTSHADE_STRENGTH, DEADLY_NIGHTSHADE_IMAGE)

    def IfPoisonous(self):
        return True