import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act(c.bck_amplitude, c.bck_frequency, c.bck_phaseOffset)
    
    def Prepare_To_Act(self, amplitude, frequency, offset):
        self.amplitute = amplitude
        self.frequency = frequency
        self.offset = offset
        
        self.motorValues = [self.amplitute, self.frequency, self.offset] # is this part right (step 82), as well as below?
        
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = frnt_sin_array[i], maxForce = 50)