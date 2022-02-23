import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as np

import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.values = None
        self.motorValues = []
        self.jointName = jointName

        self.amplitude = c.bck_amplitude
        self.frequency = c.bck_frequency
        self.offset = c.bck_phaseOffset

        self.targetAngles = np.linspace(-np.pi, 2*np.pi, 1000)

        MOTOR.Prepare_To_Act(self)
        #self.Prepare_To_Act(c.bck_amplitude, c.bck_frequency, c.bck_phaseOffset)
    
    def Prepare_To_Act(self):
        if(self.jointName == "Torso_Frontleg"):     
            for x in range(len(self.targetAngles)):
                self.motorValues.append(self.amplitude * np.sin((self.frequency * x) + self.offset))
        else:
            for x in range(len(self.targetAngles)):
                self.motorValues.append(self.amplitude * np.sin((self.frequency/2 * x) + self.offset))


    def Set_Value(self, i, robot):
        pyrosim.Set_Motor_For_Joint(robot, self.jointName, p.POSITION_CONTROL, self.motorValues[i], 20)
    
    def Save_Values(self):
        np.save("data/" + str(self.jointName) + "Joint", self.values)