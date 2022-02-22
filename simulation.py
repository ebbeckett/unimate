from world import WORLD
from robot import ROBOT
from sensor import SENSOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

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
        ROBOT.Prepare_To_Sense(self) # is this called right?
        ROBOT.Sense(self)

    def run(self): # may not have to pass self through it
        for i in range(1000):
        #for i in range(len(bck_sin_array)):
            p.stepSimulation()


            
            #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = bck_sin_array[i], maxForce = 50)
            #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition = frnt_sin_array[i], maxForce = 50)
            time.sleep(0.002)
            #print(i)
            #print(backLegSensorValues[i])
    
    def __del__(self):
        p.disconnect()



