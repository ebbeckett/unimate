from cmath import sin
from time import sleep
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import random

bck_amplitude = numpy.pi/4
bck_frequency = 0.06
bck_phaseOffset = 0

frnt_amplitude = numpy.pi/4
frnt_frequency = 0.06
frnt_phaseOffset = 0


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8) #is this working?
planeId = p.loadURDF("plane.urdf")      
robotId = p.loadURDF("body.urdf")   
p.loadSDF("world.sdf")

#0.017

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)


target_angles = numpy.linspace(-numpy.pi, 2*numpy.pi, 1000)

bck_sin_array = []
for element in range(len(target_angles)):
    bck_sin_array.append(bck_amplitude * numpy.sin((bck_frequency * element) + bck_phaseOffset))

frnt_sin_array = []
for element in range(len(target_angles)):
    frnt_sin_array.append(frnt_amplitude * numpy.sin((frnt_frequency * element) + frnt_phaseOffset))

#numpy.save(os.path.join('data','numpsin'), sin_array)


#for i in range(1000):
for i in range(len(bck_sin_array)):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")

    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = bck_sin_array[i], maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = frnt_sin_array[i], maxForce = 50)
    time.sleep(0.002)
    #print(i)
    #print(backLegSensorValues[i])

numpy.save(os.path.join('data','bcklegvalfile'), backLegSensorValues)
numpy.save(os.path.join('data','frntlegvalfile'), frontLegSensorValues)

#print(backLegSensorValues)
#print(backLegSensorValues)

p.disconnect()

