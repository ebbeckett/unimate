import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

import hillclimber as hc

# class SEARCH:
#     def __init__(self):
#         print('********* Got here in search.py *********')
#         self.hc.Evolve()

os.system("python3 parallelHillClimber.py")

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()

#os.system("python3 generate.py")
#os.system("python3 simulate.py")