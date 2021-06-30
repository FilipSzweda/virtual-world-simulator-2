import pygame
import os
from plant import Plant
from animal import Animal

SOSNOWSKYS_HOGWEED_STRENGTH = 10
SOSNOWSKYS_HOGWEED_IMAGE = pygame.image.load(os.path.join('assets', 'sosnowskys_hogweed.png'))

class SosnowskysHogweed(Plant):
    def __init__(self, world, position):
        super().__init__(world, position, SOSNOWSKYS_HOGWEED_STRENGTH, SOSNOWSKYS_HOGWEED_IMAGE)

    def IfPoisonous(self):
        return True
    
    def Action(self):
        poisonedAnimals = []

        for i in self.FindPositionsNear():
            if self.GetWorld().GetMap(self.CalculateMapIndex(i)) != None:
                if isinstance(self.GetWorld().GetMap(self.CalculateMapIndex(i)), Animal) and not isinstance(self.GetWorld().GetMap(self.CalculateMapIndex(i)), CyberSheep):
                    poisonedAnimals.append(self.GetWorld().GetMap(self.CalculateMapIndex(i)))

        for i in poisonedAnimals:
            i.RemoveFromMap(i.GetPosition())
            
        super().Action()

from animals.cyber_sheep import CyberSheep