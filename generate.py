import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z= 1.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[3, 3, 0], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
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

    #print("torso backleg pos = ", torso_backleg_pos)
    #print("torso frontleg pos = ", torso_frontleg_pos)
    #print("backleg ", backleg_pos)
    #print("front leg =", frontleg_pos)
    pyrosim.End()

Create_World()
Create_Robot()

