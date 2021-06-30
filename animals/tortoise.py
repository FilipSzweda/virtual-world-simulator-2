import pygame
import os
import random
from animal import Animal

TORTOISE_STRENGTH = 2
TORTOISE_INITIATIVE = 1
TORTOISE_IMAGE = pygame.image.load(os.path.join('assets', 'tortoise.png'))

class Tortoise(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, TORTOISE_INITIATIVE, TORTOISE_STRENGTH, TORTOISE_IMAGE)

    def Action(self):
        moveChance = random.randrange(0, 4)
        
        if moveChance == 0:
            super().Action()

    def IfDeflectedAttack(self, attackingOrganism):
        if attackingOrganism.GetStrength() < 5:
            return True
        else:
            return False