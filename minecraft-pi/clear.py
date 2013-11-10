import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

mc.postToChat("Welcome to Minecraft Pi! Clearing a play space.")
time.sleep(5)

playerTilePos = mc.player.getTilePos()
blockBelowPlayerType = mc.getBlock(playerTilePos.x, playerTilePos.y - 1, playerTilePos.z)

mc.setBlocks(playerTilePos.x - 25, playerTilePos.y - 1,
playerTilePos.z - 25, playerTilePos.x + 25, playerTilePos.y - 1,
playerTilePos.z + 25, block.STONE)

mc.setBlocks(playerTilePos.x - 25, playerTilePos.y, playerTilePos.z -
25, playerTilePos.x + 25, playerTilePos.y + 64, playerTilePos.z + 25,
block.AIR)
