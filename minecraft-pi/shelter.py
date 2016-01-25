# import modules
from mcpi.minecraft import Minecraft

# connect to MInecraft
mc = Minecraft.create()

#get player position
pos = mc.player.getPos()

#set the starting point a little away from the player
x = pos.x + 5
y = pos.y - 1
z = pos.z + 5

#define building variables
width = 10
height = 5
length = 6

blocktype = 4
air = 0

#build shelter
mc.setBlocks(x, y, z, x + width, y + height, z + length, blocktype)

#hollow it out
mc.setBlocks(x + 1, y + 1, z + 1, x +width -1, y + height -1, z + length -1, air)

#make a doorway
mc.setBlock(x + width/2, y + 1, z, air)
mc.setBlock(x + width/2, y + 2, z, air)
