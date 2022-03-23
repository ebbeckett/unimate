from cmath import sin
from time import sleep
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import constants as c
import sys

from simulation import SIMULATION
from world import WORLD
from robot import ROBOT

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitnes()








  



