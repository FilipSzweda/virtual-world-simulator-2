import pygame
import os
from plant import Plant

GUARANA_STRENGTH = 0
GUARANA_IMAGE = pygame.image.load(os.path.join('assets', 'guarana.png'))

class Guarana(Plant):
    def __init__(self, world, position):
        super().__init__(world, position, GUARANA_STRENGTH, GUARANA_IMAGE)

    def IfStrengthBonus(self):
        return True