import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)

        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
       # self.fitness = f.read()
        f.close()
        os.remove(fitnessFile)

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box2", pos=[0, 80, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box2", pos=[-3, 0, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-2, 5, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-2, -5, 0.5], size=[1, 1, 1])
        # # pyrosim.Send_Cube(name="Box3", pos=[-4, -3, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-4, -5, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-6, 0, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-2, 3, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-8, 5, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-8, -5, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-8, 2, 0.5], size=[1, 1, 1])
        # pyrosim.Send_Cube(name="Box3", pos=[-10, -5, 0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

        pyrosim.End()

    def Create_Brain(self):
        fileName = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(fileName)

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        # Motor neuron
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons -1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self):
        return self.myID