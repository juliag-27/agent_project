import random
from agent import *

class Population:
    ''' A class for modelling a custom number of Agents in a population and their interactions.

        Fields: 
        agent_list: a list of all Agents existing in the whole population
        rounds: an int representing the number of rounds that will play upon calling run()
    '''
    def __init__(self, num_agents: int = 0, num_rounds: int = None) -> None:
        self.rounds = num_rounds
        self.populate(num_agents)
    
    def populate(self, num_agents: int):
        self.agent_list = []
        self.available_agents = []
        current_ID = 1

        for i in range(num_agents):
            random_energy = int(100*random.random())
            self.agent_list.append(Agent(current_ID,random_energy))
            self.available_agents.append(current_ID)
            current_ID += 1

    def add_agent(self, agent: Agent):
        self.agent_list.append(agent)
        self.available_agents.append(agent.ID) 

    def interact(self, agent: Agent, other_agent: Agent, random: float = (random.random() + 0.5)) -> str: 
        ##Key detail: "random" determines how likely a smaller energy will overtake the larger energy. 
        ##             Random will be between 0.5 and 1.5. For instance, given two agents of energy 50, 
        ##             the second agent will have a 50% chance of gaining, and 50% chance of losing 
        ##             energy.

        if agent.energy > int(other_agent.energy*random):
            agent.gain_energy()
            other_agent.lose_energy()
            return str(agent.ID) + " gained energy from " + str(other_agent.ID)
        else:
            agent.lose_energy()
            other_agent.gain_energy()
            return str(other_agent.ID) + " gained energy from " + str(agent.ID)

    def __str__(self) -> str:
        string_to_return = ''
        for i in range(len(self.agent_list)):
            agent = self.agent_list[i]
            string_to_return += "Agent: " + str(agent.ID) + ", Energy:  " + str(agent.energy) + "\n"
        return string_to_return

    def run_once(self) -> None:
        for i in range(int(len(self.agent_list)/2)):
            random_difference = int(random.random() * (len(self.available_agents)-1)) #-1 so no agent generated twice
            agent_to_pair = self.agent_list[self.available_agents[0] - 1] ##ID of agent w/ smallest ID 
            random_other_agent = self.agent_list[self.available_agents[1 + random_difference] - 1] ##ID of agent w/next smallest ID

            self.interact(agent_to_pair, random_other_agent) #print this function to see changes in action

            self.available_agents.remove(agent_to_pair.ID)
            self.available_agents.remove(random_other_agent.ID)

        self.reset_available_agents()

    def reset_available_agents(self):
        #Clear the list in case the # agents is odd, and there is an agent left
        self.available_agents = []

        #Repopulate the list of agents able to pair w/the list of all agents
        for i in range(len(self.agent_list)):
            self.available_agents.append(self.agent_list[i].ID)
        
    def run(self) -> None:
        for i in range(self.rounds):
            self.run_once()