import numpy 
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data

class SENSOR:
    def __init__(self, linkname):
        self.linkname = linkname
        self.values = numpy.zeros(1000)
    
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)
        
        # if(i == 1000):
        #     print(self.values[i])
    
    def Save_Values(self):
        np.save("data/" + str(self.linkName) + "Sensor", self.values)