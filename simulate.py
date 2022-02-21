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

     



#0.017


#backLegSensorValues = numpy.zeros(1000)
#frontLegSensorValues = numpy.zeros(1000)


#target_angles = numpy.linspace(-numpy.pi, 2*numpy.pi, 1000)

#bck_sin_array = []
#for element in range(len(target_angles)):
    #bck_sin_array.append(c.bck_amplitude * numpy.sin((c.bck_frequency * element) + c.bck_phaseOffset))

#frnt_sin_array = []
#for element in range(len(target_angles)):
    #frnt_sin_array.append(c.frnt_amplitude * numpy.sin((c.frnt_frequency * element) + c.frnt_phaseOffset))

#numpy.save(os.path.join('data','numpsin'), sin_array)


#for i in range(1000):
#for i in range(len(bck_sin_array)):
    #p.stepSimulation()
    #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")

    
    #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = bck_sin_array[i], maxForce = 50)
    #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = frnt_sin_array[i], maxForce = 50)
    #time.sleep(0.002)
    #print(i)
    #print(backLegSensorValues[i])

#numpy.save(os.path.join('data','bcklegvalfile'), backLegSensorValues)
#numpy.save(os.path.join('data','frntlegvalfile'), frontLegSensorValues)

#print(backLegSensorValues)
#print(backLegSensorValues)

#p.disconnect()



