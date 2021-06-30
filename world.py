import pygame
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

class World:
    __turn = 0
    __specialAbilityUseTurn = -1
    __input = None
    __chosenOrganism = None
    __simulationManager = None
    __humanAlive = False
    __organisms = []
    __activeOrganisms = []
    __map = []

    def __init__(self, width, height, fields, sowProbability):
        self.__width = width
        self.__height = height
        self.__fields = fields
        self.__field = int(self.__height / self.__fields)
        self.__sowProbability = sowProbability
        self.__background = (230, 230, 230)
        self.__specialAbilityBackground = (25, 25, 25)

        for i in range (self.__fields * self.__fields):
            self.__map.append(None)

    def GetWidth(self):
        return self.__width

    def GetHeight(self):
        return self.__height

    def GetFields(self):
        return self.__fields

    def GetField(self):
        return self.__field

    def GetSowProbability(self):
        return self.__sowProbability

    def GetTurn(self):
        return self.__turn

    def GetSpecialAbilityUseTurn(self):
        return self.__specialAbilityUseTurn

    def GetOrganisms(self):
        return self.__organisms

    def SetWidth(self, width):
        self.__width = width

    def SetHeight(self, height):
        self.__height = height

    def SetFields(self, fields):
        self.__fields = fields

    def SetSowProbability(self, sowProbability):
        self.__sowProbability = sowProbability

    def SetTurn(self, turn):
        self.__turn = turn

    def SetSpecialAbilityUseTurn(self, specialAbilityUseTurn):
        self.__specialAbilityUseTurn = specialAbilityUseTurn

    def SetHumanAlive(self, humanAlive):
        self.__humanAlive = humanAlive

    def SetSimulationManager(self, simulationManager):
        self.__simulationManager = simulationManager

    def GetMap(self, index):
        return self.__map[index]

    def GetInput(self):
        return self.__input

    def SetInput(self, input):
        self.__input = input

    def IfHuman(self):
        human = False

        for i in self.__organisms:
            if isinstance(i, Human):
                human = True
                break

        if human == True:
            self.__humanAlive = True
        else:
            self.__humanAlive = False

    def ClearMap(self):
        self.__map.clear()

        for i in range (self.__fields * self.__fields):
            self.__map.append(None)

    def AddToMap(self, index, organism):
        self.__map[index] = organism

    def RemoveFromMap(self, index):
        self.__map[index] = None

    def Reset(self):
        self.__turn = 0
        self.__specialAbilityUseTurn = -1
        self.__input = None
        self.__humanAlive = False
        self.__organisms.clear()
        self.__activeOrganisms.clear()
        self.__map.clear()
        self.ClearMap()
    
    def Draw(self):
        WIN = pygame.display.set_mode((self.__width, self.__height ))
        self.DrawBackground(WIN)
        self.DrawOrganisms(WIN)
        self.DrawInterface(WIN)
        pygame.display.update()

    def DrawBackground(self, WIN):
        if self.__humanAlive == True and self.__specialAbilityUseTurn > -1 and self.__turn - self.__specialAbilityUseTurn < 5:
            WIN.fill(self.__specialAbilityBackground)
        else:
            WIN.fill(self.__background)
    
    def DrawOrganisms(self, WIN):
        for i in self.__organisms:
            i.Draw(WIN)
    
    def DrawInterface(self, WIN):
        self.DrawGeneralButtons(WIN)
        self.DrawOrganismButtons(WIN)

    def DrawGeneralButtons(self, WIN):
        pygame.draw.rect(WIN, (220, 220, 220), [self.__height, 0, self.__width-self.__height, int(self.__height / 5)])
        pygame.draw.rect(WIN, (210, 210, 210), [self.__height, int(self.__height / 5), self.__width-self.__height, int(self.__height / 5)])
        pygame.draw.rect(WIN, (200, 200, 200), [self.__height, 2 * int(self.__height / 5), self.__width-self.__height, int(self.__height / 5)])
        pygame.draw.rect(WIN, (190, 190, 190), [self.__height, 3 * int(self.__height / 5), self.__width-self.__height, int(self.__height / 5)])
        pygame.font.init()
        font = pygame.font.SysFont('Corbel', 35)
        text = font.render('Next Turn', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + int((self.__width - self.__height) / 2), int(self.__height / 10)))
        WIN.blit(text, text_rect)
        text = font.render('New Simulation', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + int((self.__width - self.__height) / 2), 3 * int(self.__height / 10)))
        WIN.blit(text, text_rect)
        text = font.render('Save Simulation', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + int((self.__width - self.__height) / 2), 5 * int(self.__height / 10)))
        WIN.blit(text, text_rect)
        text = font.render('Load Simulation', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + int((self.__width - self.__height) / 2), 7 * int(self.__height / 10)))
        WIN.blit(text, text_rect)
        
    def DrawOrganismButtons(self, WIN):
        pygame.draw.rect(WIN, (180, 180, 180), [self.__height, 4 * int(self.__height / 5), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (170, 170, 170), [self.__height + int((self.__width-self.__height) / 6), 4 * int(self.__height / 5), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (180, 180, 180), [self.__height + 2 * int((self.__width-self.__height) / 6), 4 * int(self.__height / 5), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (170, 170, 170), [self.__height + 3 * int((self.__width-self.__height) / 6), 4 * int(self.__height / 5), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (180, 180, 180), [self.__height + 4 * int((self.__width-self.__height) / 6), 4 * int(self.__height / 5), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (170, 170, 170), [self.__height + 5 * int((self.__width-self.__height) / 6), 4 * int(self.__height / 5), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (170, 170, 170), [self.__height, 4 * int(self.__height / 5) + int(self.__height / 10), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (180, 180, 180), [self.__height + int((self.__width-self.__height) / 6), 4 * int(self.__height / 5) + int(self.__height / 10), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (170, 170, 170), [self.__height + 2 * int((self.__width-self.__height) / 6), 4 * int(self.__height / 5) + int(self.__height / 10), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (180, 180, 180), [self.__height + 3 * int((self.__width-self.__height) / 6), 4 * int(self.__height / 5) + int(self.__height / 10), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (170, 170, 170), [self.__height + 4 * int((self.__width-self.__height) / 6), 4 * int(self.__height / 5) + int(self.__height / 10), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.draw.rect(WIN, (180, 180, 180), [self.__height + 5 * int((self.__width-self.__height) / 6), 4 * int(self.__height / 5) + int(self.__height / 10), int((self.__width-self.__height) / 6), int(self.__height / 10)])
        pygame.font.init()
        font = pygame.font.SysFont('Corbel', 20)
        text = font.render('Antelope', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + int((self.__width - self.__height) / 12), 9 * int(self.__height / 10) - int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('C-Sheep', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + int((self.__width - self.__height) / 6) + int((self.__width-self.__height) / 12), 9 * int(self.__height / 10) - int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Fox', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + 2 * int((self.__width - self.__height) / 6) + int((self.__width-self.__height) / 12), 9 * int(self.__height / 10) - int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Human', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + 3 * int((self.__width - self.__height) / 6) + int((self.__width-self.__height) / 12), 9 * int(self.__height / 10) - int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Sheep', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + 4 * int((self.__width - self.__height) / 6) + int((self.__width-self.__height) / 12), 9 * int(self.__height / 10) - int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Tortoise', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + 5 * int((self.__width - self.__height) / 6) + int((self.__width-self.__height) / 12), 9 * int(self.__height / 10) - int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Wolf', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + int((self.__width - self.__height) / 12), 9 * int(self.__height / 10) + int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Dandelion', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + int((self.__width - self.__height) / 6) + int((self.__width-self.__height) / 12), 9 * int(self.__height / 10) + int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Nightshade', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + 2 * int((self.__width-self.__height) / 6) + int((self.__width - self.__height) / 12), 9 * int(self.__height / 10) + int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Grass', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + 3 * int((self.__width-self.__height) / 6) + int((self.__width - self.__height) / 12), 9 * int(self.__height / 10) + int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Guarana', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + 4 * int((self.__width-self.__height) / 6) + int((self.__width - self.__height) / 12), 9 * int(self.__height / 10) + int(self.__height / 20)))
        WIN.blit(text, text_rect)
        text = font.render('Hogweed', True , (0,0,0))
        text_rect = text.get_rect(center=(self.__height + 5 * int((self.__width-self.__height) / 6) + int((self.__width - self.__height) / 12), 9 * int(self.__height / 10) + int(self.__height / 20)))
        WIN.blit(text, text_rect)
    
    def AddOrganism(self, newOrganism):
        organismAdded = False
        index = 0

        for i in self.__organisms:
            if newOrganism.GetInitiative() > i.GetInitiative():
                self.__organisms.insert(index, newOrganism)
                organismAdded = True
                break
            index+=1

        if organismAdded == False:
            self.__organisms.append(newOrganism)

    def UpdateActiveOrganisms(self):
        for i in self.__organisms:
            self.__activeOrganisms.append(i)

    def UserInput(self):
        waitForInput = True

        while waitForInput:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waitForInput = False
                    self.__simulationManager.SetRunSimulation(False)
                elif event.type == pygame.KEYDOWN and self.__humanAlive == True:
                    if event.key == pygame.K_UP:
                        self.__input = pygame.K_UP
                        waitForInput = False
                    elif event.key == pygame.K_DOWN:
                        self.__input = pygame.K_DOWN
                        waitForInput = False
                    elif event.key == pygame.K_RIGHT:
                        self.__input = pygame.K_RIGHT
                        waitForInput = False
                    elif event.key == pygame.K_LEFT:
                        self.__input = pygame.K_LEFT
                        waitForInput = False
                    elif event.key == pygame.K_SPACE:
                        if self.__specialAbilityUseTurn < 0 or self.__turn - self.__specialAbilityUseTurn > 10:
                            self.__specialAbilityUseTurn = self.__turn
                        self.Draw()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__height <= mouse[0] <= self.__width:
                        if 0 <= mouse[1] <= int(self.__height / 5):
                            waitForInput = False
                        elif int(self.__height / 5) <= mouse[1] <= 2 * int(self.__height / 5):
                            self.__simulationManager.NewSimulation()
                            self.Draw()
                        elif 2 * int(self.__height / 5) <= mouse[1] <= 3 * int(self.__height / 5):
                            self.__simulationManager.SaveSimulation()
                        elif  3 * int(self.__height / 5) <= mouse[1] <= 4 * int(self.__height / 5):
                            self.__simulationManager.LoadSimulation()
                            self.Draw()
                        elif self.__height <= mouse[0] <= self.__height + int((self.__width - self.__height) / 6):
                            if 4 * int(self.__height / 5) <= mouse[1] <= 5 * int(self.__height / 5) - int(self.__height / 10):
                                self.__chosenOrganism = 1
                            elif 4 * int(self.__height / 5) - int(self.__height / 10) <= mouse[1] <= 5 * int(self.__height / 5):
                                self.__chosenOrganism = 7
                        elif self.__height + int((self.__width - self.__height) / 6) <= mouse[0] <= self.__height + 2 * int((self.__width-self.__height) / 6):
                            if 4 * int(self.__height / 5) <= mouse[1] <= 5 * int(self.__height / 5) - int(self.__height / 10):
                                self.__chosenOrganism = 2
                            elif 4 * int(self.__height / 5) - int(self.__height / 10) <= mouse[1] <= 5 * int(self.__height / 5):
                                self.__chosenOrganism = 8
                        elif self.__height + 2 * int((self.__width - self.__height) / 6) <= mouse[0] <= self.__height + 3 * int((self.__width-self.__height) / 6):
                            if 4 * int(self.__height / 5) <= mouse[1] <= 5 * int(self.__height / 5) - int(self.__height / 10):
                                self.__chosenOrganism = 3
                            elif 4 * int(self.__height / 5) - int(self.__height / 10) <= mouse[1] <= 5 * int(self.__height / 5):
                                self.__chosenOrganism = 9
                        elif self.__height + 3 * int((self.__width-self.__height) / 6) <= mouse[0] <= self.__height + 4 * int((self.__width-self.__height) / 6):
                            if 4 * int(self.__height / 5) <= mouse[1] <= 5 * int(self.__height / 5) - int(self.__height / 10):
                                self.__chosenOrganism = 4
                            elif 4 * int(self.__height / 5) - int(self.__height / 10) <= mouse[1] <= 5 * int(self.__height / 5):
                                self.__chosenOrganism = 10
                        elif self.__height + 4 * int((self.__width-self.__height) / 6) <= mouse[0] <= self.__height + 5 * int((self.__width-self.__height) / 6):
                            if 4 * int(self.__height / 5) <= mouse[1] <= 5 * int(self.__height / 5) - int(self.__height / 10):
                                self.__chosenOrganism = 5
                            elif 4 * int(self.__height / 5) - int(self.__height / 10) <= mouse[1] <= 5 * int(self.__height / 5):
                                self.__chosenOrganism = 11
                        elif self.__height + 5 * int((self.__width-self.__height) / 6) <= mouse[0] <= self.__height + 6 * int((self.__width-self.__height) / 6):
                            if 4 * int(self.__height / 5) <= mouse[1] <= 5 * int(self.__height / 5) - int(self.__height / 10):
                                self.__chosenOrganism = 6
                            elif 4 * int(self.__height / 5) - int(self.__height / 10) <= mouse[1] <= 5 * int(self.__height / 5):
                                self.__chosenOrganism = 12
                    elif 0 <= mouse[0] <= self.__height:
                        if 0 <= mouse[1] <= self.__height:
                            self.AddChosenOrganismByMouse(mouse)

    def AddChosenOrganismByMouse(self, mouse):
        x = int(mouse[0] / self.__field)
        y = int(mouse[1] / self.__field)
        position = (x, y)

        if self.__chosenOrganism != None:
            if self.__map[position[0] + self.__fields * position[1]] == None:
                if self.__chosenOrganism == 1:
                    self.AddOrganism(Antelope(self, position))
                elif self.__chosenOrganism == 2:
                    self.AddOrganism(CyberSheep(self, position))
                elif self.__chosenOrganism == 3:
                    self.AddOrganism(Fox(self, position))
                elif self.__chosenOrganism == 4:
                    self.AddOrganism(Human(self, position))
                elif self.__chosenOrganism == 5:
                    self.AddOrganism(Sheep(self, position))
                elif self.__chosenOrganism == 6:
                    self.AddOrganism(Tortoise(self, position))
                elif self.__chosenOrganism == 7:
                    self.AddOrganism(Wolf(self, position))
                elif self.__chosenOrganism == 8:
                    self.AddOrganism(Dandelion(self, position))
                elif self.__chosenOrganism == 9:
                    self.AddOrganism(DeadlyNightshade(self, position))
                elif self.__chosenOrganism == 10:
                    self.AddOrganism(Grass(self, position))
                elif self.__chosenOrganism == 11:
                    self.AddOrganism(Guarana(self, position))
                elif self.__chosenOrganism == 12:
                    self.AddOrganism(SosnowskysHogweed(self, position))
                self.Draw()
    
    def MakeTurn(self):
        self.UpdateActiveOrganisms()

        for i in self.__activeOrganisms:
            if self.__map[i.CalculateMapIndex(i.GetPosition())] == i:
                startingPosition = i.GetPosition()
                i.Action()

                if i.IfCanMove() == True:
                    collisionHappened = False

                    for j in self.__organisms:
                        if self.__map[j.CalculateMapIndex(j.GetPosition())] == j and i != j and i.CheckCollision(j):
                            i.Collision(j, startingPosition)
                            collisionHappened = True
                            break

                    if collisionHappened == False:
                        i.RemoveFromMap(startingPosition)
                        i.AddToMap(i.GetPosition())

        aliveOrganisms = []

        for i in self.__organisms:
            if self.__map[i.CalculateMapIndex(i.GetPosition())] == i:
                aliveOrganisms.append(i)
            else:
                del i
                
        self.__organisms.clear()
        self.__activeOrganisms.clear()
        self.__organisms = aliveOrganisms
        self.IfHuman()
        self.__input = None
        self.__turn+=1

    def __del__(self):
        self.__organisms.clear()
        self.__activeOrganisms.clear()
        self.__map.clear()