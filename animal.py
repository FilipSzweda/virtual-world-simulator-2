import pygame
import random
from organism import Organism

class Animal(Organism):
    def __init__(self, world, position, initiative, strength, image):
        super().__init__(world, position, initiative, strength, image)

    def IfCanMove(self):
        return True

    def Action(self):
        if len(self.FindPositionsNear()) > 0:
            randomizedPositionIndex = random.randrange(0, len(self.FindPositionsNear()))
            self.SetPosition(self.FindPositionsNear()[randomizedPositionIndex])
    
    def Collision(self, collidingOrganism, startingPosition):
        if type(self) is type(collidingOrganism):
            self.Breeding(collidingOrganism, startingPosition)
        else:
            self.Fight(collidingOrganism, startingPosition)
