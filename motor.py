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

        self.amplitude = np.pi / 4
        self.frequency = 0.06
        self.offset = 0

        self.targetAngles = np.linspace(-np.pi, 2*np.pi, 1000)

        MOTOR.Prepare_To_Act(self)
        #self.Prepare_To_Act(c.bck_amplitude, c.bck_frequency, c.bck_phaseOffset)
    
    def Prepare_To_Act(self):
        if(self.jointName == "Torso_Frontleg"):     
            for x in range(len(self.targetAngles)):
                self.motorValues.append(self.amplitude * np.sin((self.frequency * x) + self.offset))
        else:
            for x in range(len(self.targetAngles)):
                self.motorValues.append(self.amplitude/.5 * np.sin((self.frequency * x)/0.5 + self.offset))


    def Set_Value(self, desiredAngle, robot):
        pyrosim.Set_Motor_For_Joint(robot, self.jointName, p.POSITION_CONTROL, desiredAngle, 20)
    
    def Save_Values(self):
        np.save("data/" + str(self.jointName) + "Joint", self.values)