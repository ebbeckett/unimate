from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parent = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize ):
            this_entry = SOLUTION(self.nextAvailableID)
            self.parent[i] = this_entry
            self.nextAvailableID += 1
        

        
    

    def Evolve(self, DORG):
        #self.parent.Evaluate("DIRECT")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        for key in self.parent:
            parent = self.parent[key]
            parent.Evaluate(DORG)


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()
        
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
       self.child.Mutate()


    def Select(self):
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child
    
    def Print(self):
        print("parent:", self.parent.fitness, "child:", self.child.fitness)
    
    def Show_Best(self): # no idea what this function is supposed to do
        #self.parent
        pass
        