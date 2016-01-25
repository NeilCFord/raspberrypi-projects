# Program to create a pool under where the player is standing

# import modules
from mcpi.minecraft import Minecraft
import time

# connect to MInecraft
mc = Minecraft.create()

# get player position
pos = mc.player.getPos()

# break player's position out in to seperate variables
x = pos.x
y = pos.y
z = pos.z

# define building variables
width = 10
depth = 5
length = 6

blocktype = 4
water = 9

# dig the pool
mc.setBlocks(x - width/2, y - depth, z - length/2, x + width/2, y - 1, z + length/2, blocktype)

#fill it with water
mc.setBlocks(x - ((width/2)-1), y - (depth-1), z - ((length/2)-1), x + ((width/2)-1), y - 1, z + ((length/2)-1), water)

# confirm the player is underwater
time.sleep(1)

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

block1 = mc.getBlock(x, y, z)
block2 = mc.getBlock(x, y + 1, z)

underwater = block1 == water and block2 == water

if underwater == True:
    mc.postToChat("You are now underwater!!")
