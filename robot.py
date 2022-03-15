from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK


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
        self.nn = NEURAL_NETWORK("brain.nndf")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(desiredAngle, self.robotId)
                #print("Neuron Name:", neuronName, " Joint Name:", jointName, " Desired Angle:", desiredAngle)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
    
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        xCoordinateOfLinkZero = stateOfLinkZero[0][0]
        print(xCoordinateOfLinkZero)

        xcorString = str(xCoordinateOfLinkZero)

        f = open("fitness.txt", "w")
        f.write(xcorString)
        f.close()
        exit()
    
    
