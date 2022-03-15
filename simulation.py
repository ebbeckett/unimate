from world import WORLD
from robot import ROBOT

import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import sys

class SIMULATION:
    def __init__(self, directOrGUI):
        if(directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI) 
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8) 

        self.world = WORLD()
        self.robot = ROBOT()


        #pyrosim.Prepare_To_Simulate(p.loadURDF("body.urdf"))
        #self.robot.Prepare_To_Sense()

    def Run(self):
        for i in range(1000): # used to be len(bck_sin_array))
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(0.0002)
    
    def Get_Fitnes(self):
        self.robot.Get_Fitness()

    def __del__(self):  
        p.disconnect()
