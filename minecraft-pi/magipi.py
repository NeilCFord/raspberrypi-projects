import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()
# mc.camera.setThirdPerson(entityId)

mc.postToChat("kill")
time.sleep(5)

playerPos = mc.player.getPos()
mc.player.setPos(playerPos.x, playerPos.y + 50, playerPos.z)
mc.postToChat("Don't look down")
time.sleep(5)
