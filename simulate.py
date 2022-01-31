from time import sleep
import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8) #is this working?
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")   
p.loadSDF("world.sdf")

#0.017
for i in range(10000):
    time.sleep(0.017)
    p.stepSimulation()
    print(i)

p.disconnect()