import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

playerTilePos = mc.player.getTilePos()
blockBelowPlayerType = mc.getBlock(playerTilePos.x, playerTilePos.y - 1, playerTilePos.z)

mc.setBlock(playerTilePos.x + 1, playerTilePos.y +1, playerTilePos.z, blockBelowPlayerType)
mc.setBlock(playerTilePos.x, playerTilePos.y +1, playerTilePos.z + 1, blockBelowPlayerType)
mc.setBlock(playerTilePos.x - 1, playerTilePos.y +1, playerTilePos.z, blockBelowPlayerType)
mc.setBlock(playerTilePos.x, playerTilePos.y +1, playerTilePos.z - 1, blockBelowPlayerType)

mc.postToChat("Trapped You!")
time.sleep(5)
