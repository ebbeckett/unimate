import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        #self.robotId = p.loadURDF("body.urdf")   
