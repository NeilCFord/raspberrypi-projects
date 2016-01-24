from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

mc.postToChat("Welcome to Minecraft Pi! Clearing a play space.")
time.sleep(5)

playerTilePos = mc.player.getTilePos()
blockBelowPlayerType = mc.getBlock(playerTilePos.x, playerTilePos.y - 1, playerTilePos.z)

mc.setBlocks(playerTilePos.x - 25,  -1,
playerTilePos.z - 25, playerTilePos.x + 25, -1,
playerTilePos.z + 25, block.STONE.id)

mc.setBlocks(playerTilePos.x - 25, 0, playerTilePos.z -
25, playerTilePos.x + 25, 64, playerTilePos.z + 25,
block.AIR.id)
