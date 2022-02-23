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
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, i):
        for key in self.sensors:
            self.sensors[key].Get_Value(i)
