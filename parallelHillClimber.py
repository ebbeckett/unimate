from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parent = {}
        self.nextAvailableID = 0

        for key in range(c.populationSize):
            this_entry = SOLUTION(self.nextAvailableID)
            self.parent[key] = this_entry
            self.nextAvailableID += 1
        

        
    

    def Evolve(self):
        #self.parent.Evaluate("DIRECT")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        self.Evaluate(self.parent)

        for currentGeneration in range(c.populationSize):
            self.Evolve_For_One_Generation()

        # for key in self.parent:
        #     parent = self.parent[key]
        #     parent.Evaluate(DORG)


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(self.children)
        self.Print()
        self.Select()
        
    
    def Spawn(self):
        self.children = {}
        for key in range(c.populationSize):
            self.childrent[key] = copy.deepcopy(self.parent[key])
            self.childrent[key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
       for child in range(c.populationSize):
           self.children[child].Mutate()


    def Select(self):
        for key in range(c.populationSize):
            if(self.parent.fitness > self.child.fitness):
                self.parent = self.child
    
    def Print(self):
        for key in range(c.populationSize):
            print("parent:", self.parent.fitness, "child:", self.child.fitness)
    
    def Show_Best(self): # no idea what this function is supposed to do
        #self.parent
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
        