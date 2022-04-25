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
        pyrosim.Send_Cube(name="Box2", pos=[0, 80, 0.5], size=[1, 1, 1])
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

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # Upper legs
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLegFirst", parent="Torso", child="LeftLegFirst", type="revolute", position=[-0.5, -0.1, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLegFirst", pos=[-0.5, -0.3, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLegSecond", parent="Torso", child="LeftLegSecond", type="revolute", position=[-0.5, 0.1, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLegSecond", pos=[-0.5, 0.3, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLegFirst", parent="Torso", child="RightLegFirst", type="revolute", position=[0.5, -0.1, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLegFirst", pos=[0.5, -0.3, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLegSecond", parent="Torso", child="RightLegSecond", type="revolute", position=[0.5, 0.1, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLegSecond", pos=[0.5, 0.3, 0], size=[1.0, 0.2, 0.2])

        # Lower legs
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLegFirst_LeftLowerLegFirst", parent="LeftLegFirst", child="LeftLowerLegFirst", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLegFirst", pos=[0, -0.3, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLegSecond_LeftLowerLegSecond", parent="LeftLegSecond", child="LeftLowerLegSecond", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLegSecond", pos=[0, 0.3, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLegFirst_RightLowerLegFirst", parent="RightLegFirst", child="RightLowerLegFirst", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLegFirst", pos=[0, -0.3, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLegSecond_RightLowerLegSecond", parent="RightLegSecond", child="RightLowerLegSecond", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLegSecond", pos=[0, 0.3, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        fileName = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(fileName)

        # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLegFirst")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLowerLegSecond")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLowerLegFirst")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="RightLowerLegSecond")

        # Motor neuron
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_LeftLegFirst")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_LeftLegSecond")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_RightLegFirst")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_RightLegSecond")
        pyrosim.Send_Motor_Neuron(name=12, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="LeftLegFirst_LeftLowerLegFirst")
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLegSecond_LeftLowerLegSecond")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLegFirst_RightLowerLegFirst")
        pyrosim.Send_Motor_Neuron(name=17, jointName="RightLegSecond_RightLowerLegSecond")

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