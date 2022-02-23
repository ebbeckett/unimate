from sensor import SENSOR
from motor import MOTOR

import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data

class ROBOT:
    def __init__(self):
        #self.robotId = p.loadURDF("body.urdf") 
        self.motors = {}
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.sensors[jointName] = SENSOR(jointName)
    
    def Sense(self, i):
        for key in self.sensors:
            self.sensors[key].Get_Value(i)
    
    def Prepare_To_Act(self):
        pass
