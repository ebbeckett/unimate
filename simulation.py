from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8) #is this working?   
        pyrosim.Prepare_To_Simulate(robotID)
