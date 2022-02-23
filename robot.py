from sensor import SENSOR
from motor import MOTOR

import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data

# changed to jointname and jointnamestoindicies rather than link name, causing error as of now 
class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf") 
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, i):
        for key in self.sensors:
            self.sensors[key].Get_Value(i)
    
    def Prepare_To_Act(self):
        #self.joints = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, i):
        for key in self.motors:
            self.motors[key].Set_Value(i, self.robotId)
