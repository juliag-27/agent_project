from agent import *
from population import * 

# #Example run: population of 2 agents of random energies, run twice
    # population = Population(2,2)
    # print(str(population))
    # population.run()
    # print(str(population))

# #Example run: population of 2 agents of the same energy, run twice
    # population = Population()
    # population.add_agent(Agent(1,50))
    # population.add_agent(Agent(2,50))

    # population.run_once()

population = Population(100,20)
print(str(population))
population.run()
print(str(population))