import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import sys

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGui, solutionID):
        self.directOrGui = directOrGui
        self.solutionID = solutionID

        if (directOrGui == 'DIRECT'):
            self.physicsClient = p.connect(p.DIRECT)
        elif (directOrGui == 'GUI'):
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):

        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            if self.directOrGui == 'GUI':
                time.sleep(1/240)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()