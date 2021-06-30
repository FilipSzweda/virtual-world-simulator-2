import pygame
import random
from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self, world, position, initiative, strength, image):
        self.__world = world
        self.__position = position
        self.__initiative = initiative
        self.__strength = strength
        self.__image = pygame.transform.scale(image, (self.__world.GetField(), self.__world.GetField()))
        self.AddToMap(self.__position)
        print(type(self).__name__, " appeared at position ", self.__position)
    
    @abstractmethod
    def Action(self):
        pass

    @abstractmethod
    def Collision(self, collidingOrganism, stertingPosition):
        pass

    def GetStrength(self):
        return self.__strength

    def GetInitiative(self):
        return self.__initiative
    
    def GetWorld(self):
        return self.__world

    def GetPosition(self):
        return self.__position

    def SetPosition(self, position):
        self.__position = position

    def IfDeflectedAttack(self, attackingOrganism):
        return False

    def IfEscapedFight(self):
        return False

    def IfStrengthBonus(self):
        return False

    def IfPoisonous(self):
        return False

    def IfCanMove(self):
        return False

    def IfAlzursShield(self):
        return False

    def CreateCopy(self, position):
        return type(self)(self.__world, position)

    def Draw(self, WIN):
        hitbox = pygame.Rect(self.__position[0] * self.__world.GetField(), self.__position[1] * self.__world.GetField(), self.__world.GetField(), self.__world.GetField())
        WIN.blit(self.__image, (hitbox.x, hitbox.y))

    def CalculateMapIndex(self, position):
        return int(position[0] + self.__world.GetFields() * position[1])

    def AddToMap(self, position):
        self.__world.AddToMap(self.CalculateMapIndex(position), self)
    
    def RemoveFromMap(self, position):
        self.__world.RemoveFromMap(self.CalculateMapIndex(position))

    def CheckCollision(self, organism):
        if(self.__position == organism.GetPosition()):
            return True
        else:
            return False

    def FindPositionsNear(self):
        directions = []
        positions = []
        up = (self.__position[0], self.__position[1] - 1)
        down = (self.__position[0], self.__position[1] + 1)
        right = (self.__position[0] + 1, self.__position[1])
        left = (self.__position[0] - 1, self.__position[1])
        directions.append(up)
        directions.append(down)
        directions.append(right)
        directions.append(left)

        for i in directions:
            if i[0] < self.__world.GetFields() and i[1] < self.__world.GetFields() and i[0] >= 0 and i[1] >= 0:
                positions.append(i)

        return positions

    def Breeding(self, collidingOrganism, startingPosition):
        self.__position = startingPosition
        positionsForChild = []

        for i in collidingOrganism.FindPositionsNear():
            if collidingOrganism.__world.GetMap(collidingOrganism.CalculateMapIndex(i)) == None:
                positionsForChild.append(i)

        if len(positionsForChild) > 0:
            randomizedPositionIndex = random.randrange(0, len(positionsForChild))
            collidingOrganism.__world.AddOrganism(collidingOrganism.CreateCopy(positionsForChild[randomizedPositionIndex]))

    def Fight(self, collidingOrganism, startingPosition):
        if collidingOrganism.IfPoisonous() == True:
            self.RemoveFromMap(startingPosition)
            self.RemoveFromMap(self.__position)
        else:
            if collidingOrganism.IfAlzursShield() == True:
                self.AlzursShield(startingPosition)
            else:
                if self.__strength >= collidingOrganism.GetStrength():
                    if collidingOrganism.IfDeflectedAttack(self) == True:
                        self.Deflected(startingPosition)
                    else:
                        self.RemoveFromMap(startingPosition)
                        self.AddToMap(self.__position)

                        if collidingOrganism.IfEscapedFight() == True:
                            collidingOrganism.Escape()
                        else:
                            if collidingOrganism.IfStrengthBonus() == True:
                                self.__strength+=3
                else:
                    if self.IfEscapedFight() == True:
                        self.RemoveFromMap(startingPosition)
                        self.Escape()
                    else:
                        self.RemoveFromMap(startingPosition)

    def Deflected(self, startingPosition):
        self.__position = startingPosition

    def AlzursShield(self, startingPosition):
        positionOnAlzursShield = self.__position
        self.Action()
        collisionHappened = False

        for i in self.__world.GetOrganisms():
            if self.__world.GetMap(i.CalculateMapIndex(i.GetPosition())) == i and self != i and self.CheckCollision(i):
                self.Collision(i, startingPosition)
                collisionHappened = True
                break

        if collisionHappened == False:
            self.RemoveFromMap(startingPosition)
            self.AddToMap(self.__position)
        elif collisionHappened == True:
            if self.__position == positionOnAlzursShield:
                self.RemoveFromMap(startingPosition)

    def Escape(self):
        escapePositions = []

        for i in self.FindPositionsNear():
            if self.__world.GetMap(self.CalculateMapIndex(i)) == None:
                escapePositions.append(i)
                
        randomizedPositionIndex = random.randrange(0, len(escapePositions))
        self.__position = self.FindPositionsNear()[randomizedPositionIndex]
        self.AddToMap(self.__position)
    
    def __del__(self):
        print(type(self).__name__, " died at position ", self.__position)