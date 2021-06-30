import pygame
import os
import random
from animal import Animal

CYBER_SHEEP_STRENGTH = 11
CYBER_SHEEP_INITIATIVE = 4
CYBER_SHEEP_IMAGE = pygame.image.load(os.path.join('assets', 'cyber_sheep.png'))

class CyberSheep(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, CYBER_SHEEP_INITIATIVE, CYBER_SHEEP_STRENGTH, CYBER_SHEEP_IMAGE)

    def Action(self):
        up = (self.GetPosition()[0], self.GetPosition()[1] - 1)
        down = (self.GetPosition()[0], self.GetPosition()[1] + 1)
        right = (self.GetPosition()[0] + 1, self.GetPosition()[1])
        left = (self.GetPosition()[0] - 1, self.GetPosition()[1])
        closestDistance = self.GetWorld().GetFields() * self.GetWorld().GetFields()
        foundSosnowskysHogweed = False
        
        for i in self.GetWorld().GetOrganisms():
            if isinstance(i, SosnowskysHogweed):
                foundSosnowskysHogweed = True
                distance = i.GetPosition()[0] + i.GetPosition()[1]
                if distance < closestDistance:
                    closestDistance = distance
                    positionSosnowskysHogweed = (i.GetPosition()[0], i.GetPosition()[1])
        
        if foundSosnowskysHogweed == True:
            direction = random.randrange(0, 2)
            
            if direction == 0:
                if self.GetPosition()[0] > positionSosnowskysHogweed[0]:
                    self.SetPosition(left)
                elif self.GetPosition()[0] < positionSosnowskysHogweed[0]:
                    self.SetPosition(right)
            else:
                if self.GetPosition()[1] > positionSosnowskysHogweed[1]:
                    self.SetPosition(up)
                elif self.GetPosition()[1] < positionSosnowskysHogweed[1]:
                    self.SetPosition(down)
        else:
            super().Action()

    def Collision(self, collidingOrganism, startingPosition):
        if type(self) is type(collidingOrganism):
            self.Breeding(collidingOrganism, startingPosition)
        elif isinstance(collidingOrganism, SosnowskysHogweed):
            self.RemoveFromMap(startingPosition)
            self.AddToMap(self.GetPosition())
        else:
            self.Fight(collidingOrganism, startingPosition)

from plants.sosnowskys_hogweed import SosnowskysHogweed