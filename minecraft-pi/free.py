import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()
playerTilePos = mc.player.getTilePos()
blockBelowPlayerType = mc.getBlock(playerTilePos.x, playerTilePos.y - 1, playerTilePos.z)

mc.setBlock(playerTilePos.x + 1, playerTilePos.y +1, playerTilePos.z, block.AIR)

mc.postToChat("Be Free")
time.sleep(5)
a
