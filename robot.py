from re import S
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        self.motors = {}
        #self.robotId = p.loadURDF("body.urdf")   
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices: # is this for loop here or simulation?
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self):
        #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
        for key in self.sensors:
            SENSOR.Get_Value(self) # this may be wrong
            print(key)
        