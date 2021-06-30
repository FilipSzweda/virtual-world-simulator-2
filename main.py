import pygame
from simulation_manager import SimulationManager
from world import World

def main():
    pygame.display.set_caption("Virtual World Simulator 2.0")
    settings = input("Choose simulation settings: d - default, c - custom:\n")
    
    while settings != "d" and settings != "c":
        settings = input("Choose simulation settings: d - default, c - custom:\n")
    
    if settings == "d":
        width = 1280
        height = 720
        fields =  20
        sowProbability = 0.15
    else:
        width = int(input("Set window width:\n"))
        height = int(input("Set window height:\n"))
        fields =  int(input("Set fields of the simulation board:\n"))
        sowProbability = float(input("Set sow probability (0 <= float <= 1):\n"))
    
    world = World(width, height, fields, sowProbability)
    simulation = SimulationManager(world)
    world.SetSimulationManager(simulation)
    simulation.NewSimulation()
    simulation.Simulate() 

if __name__ == "__main__":
    main()