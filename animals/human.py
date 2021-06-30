import pygame
import os
from animal import Animal

HUMAN_STRENGTH = 5
HUMAN_INITIATIVE = 4
HUMAN_IMAGE = pygame.image.load(os.path.join('assets', 'human.png'))

class Human(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, HUMAN_INITIATIVE, HUMAN_STRENGTH, HUMAN_IMAGE)
        self.GetWorld().SetHumanAlive(True)

    def Action(self):
        up = (self.GetPosition()[0], self.GetPosition()[1] - 1)
        down = (self.GetPosition()[0], self.GetPosition()[1] + 1)
        right = (self.GetPosition()[0] + 1, self.GetPosition()[1])
        left = (self.GetPosition()[0] - 1, self.GetPosition()[1])

        if self.GetWorld().GetInput() == pygame.K_UP:
            if up[1] >= 0:
                self.SetPosition(up)
        elif self.GetWorld().GetInput() == pygame.K_DOWN:
            if down[1] < self.GetWorld().GetFields():
                self.SetPosition(down)
        elif self.GetWorld().GetInput() == pygame.K_RIGHT:
            if right[0] < self.GetWorld().GetFields():
                self.SetPosition(right)
        elif self.GetWorld().GetInput() == pygame.K_LEFT:
            if left[0] >= 0:
                self.SetPosition(left)

    def IfAlzursShield(self):
        if self.GetWorld().GetTurn() - self.GetWorld().GetSpecialAbilityUseTurn() < 5 and self.GetWorld().GetSpecialAbilityUseTurn() > -1:
            return True
        else:
            return False