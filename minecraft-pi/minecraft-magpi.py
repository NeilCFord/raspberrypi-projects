from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

mc.postToChat("Hello Minecraft World")
time.sleep(5)

playerPos = mc.player.getPos()

#Changing your players position
mc.postToChat("Move your player - 30 blocks UP!")
time.sleep(2)
mc.player.setPos(playerPos.x,playerPos.y + 30,playerPos.z)
mc.postToChat("Don't look down!")
# - wait for you to fall!
time.sleep(5)

