import random
from organism import Organism

PLANT_INITIATIVE = 0

class Plant(Organism):
    def __init__(self, world, position, strength, image):
        super().__init__(world, position, PLANT_INITIATIVE, strength, image)

    def Action(self):
        sowChance = random.randrange(0, int(1 / self.GetWorld().GetSowProbability()))

        if sowChance == 0:
            positionsForChild = []

            for i in self.FindPositionsNear():
                if self.GetWorld().GetMap(self.CalculateMapIndex(i)) == None:
                    positionsForChild.append(i)
                    
            if len(positionsForChild) > 0:
                randomizedPositionIndex = random.randrange(0, len(positionsForChild))
                self.GetWorld().AddOrganism(self.CreateCopy(positionsForChild[randomizedPositionIndex]))
    
    def Collision(self, collidingOrganism, startingPosition):
        self.RemoveFromMap(startingPosition)
