import os
from hillclimber import HILL_CLIMBER


for i in range(1):
    # os.system("python3 generate.py")
    # os.system("python3 simulate.py")
    os.system("python3 hillclimber.py")

hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()