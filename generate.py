import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z= 1.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[3, 3, 0.5], size=[length, width, height])
    pyrosim.End()

# def Create_Robot():


def Generate_Body():

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

    # print("torso backleg pos = ", torso_backleg_pos)
    # print("torso frontleg pos = ", torso_frontleg_pos)
    # print("backleg ", backleg_pos)
    # print("front leg =", frontleg_pos)
    pyrosim.End()

def Generate_Brain():
    
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
    
    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()
#Create_Robot()

