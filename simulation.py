from world import WORLD
from robot import ROBOT

import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8) 

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(p.loadURDF("body.urdf"))
        self.robot.Prepare_To_Sense()

    def Run(self):
        for i in range(1000): # used to be len(bck_sin_array))
            p.stepSimulation()
            self.robot.Sense(i)



            # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = bck_sin_array[i], maxForce = 50)
            # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = frnt_sin_array[i], maxForce = 50)
            time.sleep(0.017)
    #print(i)
    #print(backLegSensorValues[i])

    def __del__(self):  
        p.disconnect()
