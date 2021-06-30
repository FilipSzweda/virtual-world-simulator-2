import pygame
import random
from animals.antelope import Antelope
from animals.cyber_sheep import CyberSheep
from animals.fox import Fox
from animals.human import Human
from animals.sheep import Sheep
from animals.tortoise import Tortoise
from animals.wolf import Wolf
from plants.dandelion import Dandelion
from plants.deadly_nightshade import DeadlyNightshade
from plants.grass import Grass
from plants.guarana import Guarana
from plants.sosnowskys_hogweed import SosnowskysHogweed

class SimulationManager:
    __runSimulation = True

    def __init__(self, world):
        self.__world = world
    
    def SetRunSimulation(self, runSimulation):
        self.__runSimulation = runSimulation

    def NewSimulation(self):
        self.__world.Reset()
        humanPosition = (0,0)
        self.__world.AddOrganism(Human(self.__world, humanPosition))

        for i in range(self.__world.GetFields()):
            for j in range(self.__world.GetFields()):
                position = (j, i)

                if position != (0, 0):
                    randomizedOrganism = random.randrange(0, 11)

                    if(randomizedOrganism == 0):
                        self.__world.AddOrganism(SosnowskysHogweed(self.__world, position))
                    elif(randomizedOrganism == 1):
                        self.__world.AddOrganism(Guarana(self.__world, position))
                    elif(randomizedOrganism == 2):
                        self.__world.AddOrganism(Dandelion(self.__world, position))
                    elif(randomizedOrganism == 3):
                        self.__world.AddOrganism(Grass(self.__world, position))
                    elif(randomizedOrganism == 4):
                        self.__world.AddOrganism(DeadlyNightshade(self.__world, position))
                    elif(randomizedOrganism == 5):
                        self.__world.AddOrganism(Antelope(self.__world, position))
                    elif(randomizedOrganism == 6):
                        self.__world.AddOrganism(CyberSheep(self.__world, position))
                    elif(randomizedOrganism == 7):
                        self.__world.AddOrganism(Fox(self.__world, position))
                    elif(randomizedOrganism == 8):
                        self.__world.AddOrganism(Sheep(self.__world, position))
                    elif(randomizedOrganism == 9):
                        self.__world.AddOrganism(Wolf(self.__world, position))
                    elif(randomizedOrganism == 10):
                        self.__world.AddOrganism(Tortoise(self.__world, position))

    def SaveSimulation(self):
        save = open("save.txt", "w")
        save.write(str(self.__world.GetWidth()) + " " + str(self.__world.GetHeight()) + " " + str(self.__world.GetFields()) + " " + str(self.__world.GetSowProbability()) + " " + str(self.__world.GetTurn()) + " " + str(self.__world.GetSpecialAbilityUseTurn()) + "\n")

        for i in self.__world.GetOrganisms():
            save.write(type(i).__name__ + " " + str(i.GetPosition()[0]) + " " + str(i.GetPosition()[1]) + " " + str(i.GetStrength()) + "\n")

        save.close()

    def LoadSimulation(self):
        self.__world.Reset()
        save = open("save.txt", "r")
        data = save.read().replace("\n", " ").split()
        index = 0

        for i in data:
            if index < 6:
                if index == 0:
                    self.__world.SetWidth(int(i))
                elif index == 1:
                    self.__world.SetHeight(int(i))
                elif index == 2:
                    self.__world.SetFields(int(i))
                    self.__world.ClearMap()
                elif index == 3:
                    self.__world.SetSowProbability(float(i))
                elif index == 4:
                    self.__world.SetTurn(int(i))
                elif index == 5:
                    self.__world.SetSpecialAbilityUseTurn(int(i))
            elif index % 4 == 2:
                name = str(i)
            elif index % 4 == 3:
                x = int(i)
            elif index % 4 == 0:
                y = int(i)
            elif index % 4 == 1:
                strength = int(i)

                if(name == 'SosnowskysHogweed'):
                    loadedOrganism = SosnowskysHogweed(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Guarana"):
                    loadedOrganism = Guarana(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Dandelion"):
                    loadedOrganism = Dandelion(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Grass"):
                    loadedOrganism = Grass(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "DeadlyNightshade"):
                    loadedOrganism = DeadlyNightshade(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Antelope"):
                    loadedOrganism = Antelope(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "CyberSheep"):
                    loadedOrganism = CyberSheep(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Human"):
                    loadedOrganism = Human(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Fox"):
                    loadedOrganism = Fox(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Sheep"):
                    loadedOrganism = Sheep(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Wolf"):
                    loadedOrganism = Wolf(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)
                elif(name == "Tortoise"):
                    loadedOrganism = Tortoise(self.__world, (x, y))
                    loadedOrganism.strength = strength
                    self.__world.AddOrganism(loadedOrganism)

            index+=1

        save.close()

    def Simulate(self):
        while self.__runSimulation:
            self.__world.Draw()
            self.__world.UserInput()
            self.__world.MakeTurn()
            
        pygame.quit()

    def __del__(self):
        del self.__world
