import random

class Agent:
    ''' A class for modelling agents with unique IDs, energy level, and capability for 
        exchanging energy with other agents based on the energy level.

        Fields:
        ID: an int representing a unique ID. When in a Population, this ID will be unique from other Agents
        energy: a float representing an energy level '''
    
    '''Constructor for an Agent. Assumes a unique ID and energy level has already been generated
    
    Parameters:
    id -- a unique ID that represents an Agent. when created in a population, will be unique from all other agents
    energy -- (default 0) the level of energy that an Agent has, 0-99. The higher the energy, the more likely it will take
                energy from other Agents during interactions
    '''
    def __init__(self, id_num: int, energy: int = 0) -> None:
        self.ID = id_num
        self.energy = energy
    
    def gain_energy(self) -> None:
        ''' Adds a constant level of energy to the agent'''
        self.energy += 5
    
    def lose_energy(self) -> None:
        ''' Removes a constant level of energy from the agent'''
        self.energy += -5

    def __str__(self):
        return "Agent " + self.ID + " with energy " + str(self.energy)