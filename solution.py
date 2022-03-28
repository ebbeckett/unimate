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
        self.weights = self.weights * c.numMotorNeurons - 1
      #  print(self.weights)

    def Evaluate(self, directOrGui):
        pass

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)

        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
     #   print("FiTNESS " + str(self.fitness))
        f.close()
        os.remove(fitnessFile)

    def Create_World(self):
        length = 1
        width = 1
        height = 1

        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[3, 3, 0.5], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        length = 1
        width = 1
        height = 1

        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="Leftleg", type="revolute", position=[-0.5, 0, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Leftleg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="Rightleg", type="revolute", position=[0.5, 0, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Rightleg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
       
        pyrosim.Send_Joint(name="Frontleg_FrontlowerLeg", parent="FrontLeg", child="FrontLowerleg", type="revolute", position=[0, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerleg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name="Backleg_BacklowerLeg", parent="Backleg", child="BackLowerleg", type="revolute", position=[0, -0.5, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerleg", pos=[0, -0.5, -0.5], size=[0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name="Leftleg_Leftlowerleg", parent="Leftleg", child="LeftLowerleg", type="revolute", position=[-0.5, 0, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLowerleg", pos=[-0.5, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Rightleg_RightLowerleg", parent="Rightleg", child="RightLowerleg", type="revolute", position=[0.5, 0, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLowerleg", pos=[0.5, 0, -0.5], size=[0.2, 0.2, 1])
      
        pyrosim.End()

    def Create_Brain(self):
        fileName = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(fileName)

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="Leftleg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="Rightleg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerleg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerleg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LeftLowerleg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="RightLowerleg")


        # Motor neuron
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Frontleg_FrontlowerLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Backleg_BacklowerLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Leftleg_Leftlowerleg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Rightleg_RightLowerleg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
        

    def Mutate(self):
        randomRow = random.randint(0, c.numMotorNeurons)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * c.numMotorNeurons - 1

    def Set_ID(self):
        return self.myID