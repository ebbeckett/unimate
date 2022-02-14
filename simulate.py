from time import sleep
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8) #is this working?
planeId = p.loadURDF("plane.urdf")      
robotId = p.loadURDF("body.urdf")   
p.loadSDF("world.sdf")

#0.017

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = 0.0, maxForce = 500)
    time.sleep(0.017)
    #print(i)
    #print(backLegSensorValues[i])

numpy.save(os.path.join('data','bcklegvalfile'), backLegSensorValues)
numpy.save(os.path.join('data','frntlegvalfile'), frontLegSensorValues)

#print(backLegSensorValues)
#print(backLegSensorValues)

p.disconnect()

