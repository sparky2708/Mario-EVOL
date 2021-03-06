import sys
import nintaco
import logging as log
#log.basicConfig(filename="D:\\temp\\debug.log")
from mario_game import MarioGame

_screen_height = 240
_screen_width = 256

nintaco.initRemoteAPI("localhost", 9999)
api = nintaco.getAPI()
game = MarioGame(api)

def launch():
  api.addFrameListener(renderFinished)
  api.addStatusListener(statusChanged)
  api.addActivateListener(apiEnabled)
  api.addDeactivateListener(apiDisabled)
  api.addStopListener(dispose)
  api.run()
  
def apiEnabled():
  global _screen_height
  global _screen_width

  log.debug("API enabled")

  # sprite = [0 for i in range(SPRITE_SIZE * SPRITE_SIZE)]
  # for y in range(SPRITE_SIZE):
  #   Y = y - SPRITE_SIZE / 2 + 0.5
  #   for x in range(SPRITE_SIZE):
  #     X = x - SPRITE_SIZE / 2 + 0.5
  #     sprite[SPRITE_SIZE * y + x] = nintaco.ORANGE if (X * X + Y * Y 
  #         <= SPRITE_SIZE * SPRITE_SIZE / 4) else -1
  # api.createSprite(SPRITE_ID, SPRITE_SIZE, SPRITE_SIZE, sprite)
  # strWidth = api.getStringWidth(STRING, False)
  # strX = (256 - strWidth) / 2
  # strY = (240 - 8) / 2
  
def apiDisabled():
  log.debug("API disabled")
  
def dispose():
  log.debug("API stopped")
  
def statusChanged(message):
  log.debug("Status message: %s" % message)
  
def renderFinished():
  global _screen_height, _screen_width, game

  api.setColor(nintaco.BLUE)
  api.fill3DRect(0, 0, _screen_width/4, _screen_height/5, True)

  print("Lives {}".format(game.getLives()))
  print("Score {}".format(game.getScore()))
  print("Coins {}".format(game.getCoins()))
  # api.drawSprite(SPRITE_ID, spriteX, spriteY)
  # if spriteX + SPRITE_SIZE == 255:
  #   spriteVx = -1
  # elif spriteX == 0:
  #   spriteVx = 1
  # if spriteY + SPRITE_SIZE == 231:
  #   spriteVy = -1
  # elif spriteY == 8:
  #   spriteVy = 1
  # spriteX += spriteVx
  # spriteY += spriteVy

  # api.setColor(nintaco.DARK_BLUE)
  # api.fillRect(strX - 1, strY - 1, strWidth + 2, 9)
  # api.setColor(nintaco.BLUE)
  # api.drawRect(strX - 2, strY - 2, strWidth + 3, 10)
  # api.setColor(nintaco.WHITE)
  # api.drawString(STRING, strX, strY, False)
  
if __name__ == "__main__":
  launch()
