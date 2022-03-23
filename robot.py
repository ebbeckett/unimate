from fileinput import filename
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data

# changed to jointname and jointnamestoindicies rather than link name, causing error as of now 
class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.motors = {}
        self.sensors = {}

        self.robotId = p.loadURDF("body.urdf") 
        fileName = "brain" + str(self.solutionID) + ".nndf"
        print(fileName)

        self.nn = NEURAL_NETWORK(fileName)

        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)

        os.remove(fileName)
        

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
        #self.nn.Print()
    
    def Get_Fitness(self):
        self.stateOfLinkZero = p.getLinkState(self.robotId,0)
        self.posLinkZero = self.stateOfLinkZero[0]
        self.xCordLinkZero = self.posLinkZero[0]
        
        fitnessFile = "fitness" + str(self.solutionID) + ".txt"
        tempFile = "tmp" + str(self.solutionID) + ".txt"
        f = open(fitnessFile, "w")

        f.write(str(self.xCordLinkZero))
        f.close()
        exit()

    
    
