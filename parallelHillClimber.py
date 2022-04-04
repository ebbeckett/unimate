from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')

     #   os.remove('brain*.nndf')
       # os.remove('fitness0.txt')

        self.parents = {}
        self.nextAvailableID = 0
        for key in range(0, c.populationSize):
            self.parents[key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
           # print(self.parents)

    def Evolve(self):

        self.Evaluate(self.parents)

        for currentGeneration in range(c.populationSize):
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
            if (self.parents[key].fitness > self.children[key].fitness): # change 1
                self.parents = self.children

    def Print(self):
        print(" ")
        for key in range(c.populationSize):
            print('Parent fitness: ', self.parents[key].fitness, ', Child fitness:', self.children[key].fitness)
        print(" ")

    def Show_Best(self):

        self.Select()
        mostFitKey = 0
        for key in range(c.populationSize-1):
            if (self.parents[key].fitness > self.parents[key+1].fitness): # change two
                mostFitKey = key+1 
        self.parents[mostFitKey].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for key in range(0, c.populationSize):
            solutions[key].Start_Simulation("DIRECT")

        for key in range(0, c.populationSize):
            solutions[key].Wait_For_Simulation_To_End()
        