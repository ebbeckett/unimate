import numpy as np
from generate import Create_World, Generate_Body, Generate_Brain
import pyrosim.pyrosim as pyrosim
import random
import os
class SOLUTION:

    def __init__(self):
        self.weights = np.array([[np.random.rand(),np.random.rand()], [np.random.rand(),np.random.rand()], [np.random.rand(), np.random.rand()]])
        self.weights = self.weights * 2 - 1
    
    def Evaluate(self):
        Create_World()
        Generate_Body()
        Generate_Brain()

        os.system("python3 simulate.py")

        f = open("fitness.txt", "r")
        readString = f.read()
        f.close() # might break here
        readFloat = float(readString)

        self.fitness = readFloat



    def Create_World():
        length = 1
        width = 1
        height = 1

        x = 0
        y = 0
        z= 1.5

        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[3, 3, 0.5], size=[length, width, height])
        pyrosim.End()

    def Generate_Body():
        length = 1
        width = 1
        height = 1

        x = 0
        y = 0
        z= 1.5

        torso_backleg_pos = [x-(0.5*length),y,z-(height/2)]
        backleg_pos = [-length/2, y, -height/2]
        frontleg_pos = [length/2, y, -height/2]
        torso_frontleg_pos = [x+(0.5*length),y,z-(height/2)]

        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[x, y, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name = "Torso_Backleg", parent= "Torso", child = "Backleg", type = "revolute", position = torso_backleg_pos)
        pyrosim.Send_Cube(name="Backleg", pos=backleg_pos, size=[length, width, height])
        pyrosim.Send_Joint(name = "Torso_Frontleg", parent= "Torso", child = "Frontleg", type = "revolute", position = torso_frontleg_pos)
        pyrosim.Send_Cube(name="Frontleg", pos=frontleg_pos, size=[length, width, height])    

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")

        for currentRow in range(3):
            for currentColumn in range(2):
                randNum = random.randint(-1,1)
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
    
    def Mutate(self):
        randomRow = random.randint(1,3)
        randomCol = random.randint(1,2)
        self.weights[randomRow, randomCol] = random.random()*2 - 1 # might brake here
        
