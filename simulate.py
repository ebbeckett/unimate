from time import sleep
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8) #is this working?
planeId = p.loadURDF("plane.urdf")      
robotId = p.loadURDF("body.urdf")   
p.loadSDF("world.sdf")

#0.017
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(10000)

for i in range(10000):
    time.sleep(0.017)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    #print(i)

print(backLegSensorValues)


p.disconnect()