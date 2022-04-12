import numpy as np
#from constants import CONSTANTS
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):

        self.values = None

        self.motorValues = []
        self.jointName = jointName

        self.amplitude = -np.pi / 4
        self.frequency = 0.06
        self.offset = 0

        self.targetAngles = np.linspace(-np.pi, 2 * np.pi, 1000)

    def Set_Value(self, desiredAngle, robot):
        pyrosim.Set_Motor_For_Joint(robot, self.jointName, p.POSITION_CONTROL, desiredAngle, 20)

    