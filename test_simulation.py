import pytest 
import random
from agent import *
from population import *

def test_agent_constructor():
    #Tests to make sure that Agents are constructed correctly
    random_num = int(random.random()*100)
    one = Agent(1, random_num)
    assert one.energy == random_num
    assert one.ID == 1

def test_agent_energy_changes():
    #Makes sure that energy level changes
    one = Agent(1,50)
    one.gain_energy()
    assert one.energy == 55
    one.lose_energy()
    assert one.energy == 50

def test_interaction():
    #Makes sure that higher energy level gives higher potential for taking energy
    one = Agent(1,50)
    two = Agent(2,60)
    population = Population(2,1) #2,1 does not matter here
    assert population.interact(one,two,1) == "2 gained energy from 1" #one will always be smaller 
    assert one.energy == 45
    assert two.energy == 65
    assert population.interact(one,two,-1) == "1 gained energy from 2" #two will always be smaller
    assert one.energy == 50
    assert two.energy == 60

def test_populate():
    #Makes sure populate method works
    population = Population(2,1)
    assert 1 + 1 == 2 #use debug mode to read agent fields 
    assert len(population.agent_list) == 2
    assert len(population.available_agents) == 2

def test_simulation():
    population = Population(2,2)
    population.run()
