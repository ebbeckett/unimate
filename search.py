import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

os.system("python3 parallelHillClimber.py")

#for i in range(1):
    # os.system("python3 generate.py")
    # os.system("python3 simulate.py")
    # os.system("python3 parallelHillClimber.py")


phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()