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
from simulation import SIMULATION

simulation = SIMULATION()
simulation.run()

     



#0.017





#target_angles = numpy.linspace(-numpy.pi, 2*numpy.pi, 1000)

#bck_sin_array = []
#for element in range(len(target_angles)):
    #bck_sin_array.append(c.bck_amplitude * numpy.sin((c.bck_frequency * element) + c.bck_phaseOffset))

#frnt_sin_array = []
#for element in range(len(target_angles)):
    #frnt_sin_array.append(c.frnt_amplitude * numpy.sin((c.frnt_frequency * element) + c.frnt_phaseOffset))

#numpy.save(os.path.join('data','numpsin'), sin_array)



#numpy.save(os.path.join('data','bcklegvalfile'), backLegSensorValues)
#numpy.save(os.path.join('data','frntlegvalfile'), frontLegSensorValues)

#print(backLegSensorValues)
#print(backLegSensorValues)




