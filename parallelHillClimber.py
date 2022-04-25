from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')

        self.parents = {}
        self.nextAvailableID = 0
        for key in range(0, c.populationSize):
            self.parents[key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        self.currentGeneration = 0

        self.ABTestArray = np.zeros((5,5)) # might brake


        

    def Evolve(self):

        self.Evaluate(self.parents)

        for self.currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):

        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in range (c.populationSize):
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in range(c.populationSize):
            self.children[child].Mutate()

    def Select(self):

        for key in range(c.populationSize):
            if (self.parents[key].fitness > self.children[key].fitness):
                self.parents = self.children

    def Print(self):
        print(" ")
        for key in range(c.populationSize):
            pass
            #print('Parent fitness: ', self.parents[key].fitness, ', Child fitness:', self.children[key].fitness)
        #print(" ")

    def Show_Best(self):

        self.Select()
        mostFitKey = 0
        for key in range(c.populationSize-1):
            if (self.parents[key].fitness > self.parents[key+1].fitness):
                mostFitKey = key+1
        self.parents[mostFitKey].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for key in range(0, c.populationSize):
            solutions[key].Start_Simulation("DIRECT")

        for key in range(0, c.populationSize):
            solutions[key].Wait_For_Simulation_To_End()
            self.ABTestArray[self.currentGeneration, key] = solutions[key].fitness
        
        print(self.ABTestArray)


        
        