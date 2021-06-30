import pygame
import os
import random
from animal import Animal

FOX_STRENGTH = 3
FOX_INITIATIVE = 7
FOX_IMAGE = pygame.image.load(os.path.join('assets', 'fox.png'))

class Fox(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, FOX_INITIATIVE, FOX_STRENGTH, FOX_IMAGE)

    def Action(self):
        notStrongerFields = []
        
        for i in self.FindPositionsNear():
            if self.GetWorld().GetMap(self.CalculateMapIndex(i)) != None:
                if self.GetWorld().GetMap(self.CalculateMapIndex(i)).GetStrength() <= self.GetStrength():
                    notStrongerFields.append(i)
            else:
                notStrongerFields.append(i)
        
        if len(notStrongerFields) > 0:
            randomizedPositionIndex = random.randrange(0, len(notStrongerFields))
            self.SetPosition(notStrongerFields[randomizedPositionIndex])