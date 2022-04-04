import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

import hillclimber as hc

os.system("python3 parallelHillClimber.py")

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()

#os.system("python3 generate.py")
#os.system("python3 simulate.py")