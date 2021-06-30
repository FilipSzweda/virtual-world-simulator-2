import pygame
import os
import random
from animal import Animal

ANTELOPE_STRENGTH = 4
ANTELOPE_INITIATIVE = 4
ANTELOPE_IMAGE = pygame.image.load(os.path.join('assets', 'antelope.png'))

class Antelope(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, ANTELOPE_INITIATIVE, ANTELOPE_STRENGTH, ANTELOPE_IMAGE)

    def Action(self):
        furtherDirections = []
        furtherPositions = []
        furtherUp = (self.GetPosition()[0], self.GetPosition()[1] - 2)
        furtherDown = (self.GetPosition()[0], self.GetPosition()[1] + 2)
        furtherRight = (self.GetPosition()[0] + 2, self.GetPosition()[1])
        furtherLeft = (self.GetPosition()[0] - 2, self.GetPosition()[1])
        furtherDirections.append(furtherUp)
        furtherDirections.append(furtherDown)
        furtherDirections.append(furtherRight)
        furtherDirections.append(furtherLeft)

        for i in furtherDirections:
            if(i[0] < self.GetWorld().GetFields() and i[1] < self.GetWorld().GetFields() and i[0] >= 0 and i[1] >= 0):
                furtherPositions.append(i)
        
        if len(furtherPositions) > 0:
            randomizedPositionIndex = random.randrange(0, len(furtherPositions))
            self.SetPosition(furtherPositions[randomizedPositionIndex])
        else:
            super().Action()
        
    def IfEscapedFight(self):
        escapeChance = random.randrange(0, 3)

        if escapeChance == 0:
            for i in self.FindPositionsNear():
                if self.GetWorld().GetMap(self.CalculateMapIndex(i)) == None:
                    return True
        
        return False