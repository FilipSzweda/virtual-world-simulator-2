import pygame
import os
from plant import Plant

DANDELION_STRENGTH = 0
DANDELION_IMAGE = pygame.image.load(os.path.join('assets', 'dandelion.png'))

class Dandelion(Plant):
    def __init__(self, world, position):
        super().__init__(world, position, DANDELION_STRENGTH, DANDELION_IMAGE)

    def Action(self):
        for i in range(3):
            super().Action()