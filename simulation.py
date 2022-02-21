from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8) #is this working?
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
        self.world = WORLD()
        self.robot = ROBOT()
        
    
        pyrosim.Prepare_To_Simulate(p.loadURDF("body.urdf")) # may be an error


