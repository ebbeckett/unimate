import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z= 0.5

pyrosim.Start_SDF("boxes.sdf")

#counter = 0
xax = 0
yax = 0

#pyrosim.Send_Cube(name="Box", pos=[x+xax, y+yax, z+counter], size=[length, width, height])

for e in range(5):
    for a in range(5):
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+a, y+e, z+i], size=[length, width, height])
            width = width*0.9
            length = length*0.9
            height = height*0.9
        length = 1
        width = 1
        height = 1







pyrosim.End()