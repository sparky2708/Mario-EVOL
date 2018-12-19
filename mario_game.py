import nintaco
import math

class MarioGame():
    marioX = None
    marioY = None

    def __init__(self, api):
        self.api = api

    def getPositions(self):
        global marioX, marioY
        marioX = self.api.peekCPU16(0x94) 
        marioY = self.api.peekCPU16(0x96)	
        
        layer1x = self.api.peekCPU16(0x1A)
        layer1y = self.api.peekCPU16(0x1C)	
        
        screenX = marioX-layer1x
        screenY = marioY-layer1y
        return screenX, screenY

    def getCoins(self):
        coins = self.api.peekCPU(0x0DBF)
        return coins

    def getScore(self):
        scoreLeft = self.api.peekCPU16(0x0F34)
        scoreRight = self.api.peekCPU16(0x0F36)
        score = ( scoreLeft * 10 ) + scoreRight
        return score

    def getLives(self):
        lives = self.api.peekCPU(0x0DBE) + 1
        return lives

    def writeLives(self, lives):
        self.api.writeCPU(0x0DBE, lives - 1)

    def getPowerup(self):
        powerup = self.api.peekCPU(0x0019)
        return powerup

    def writePowerup(self, powerup):
        self.api.writeCPU(0x0019, powerup)

    def getMarioHit(self, alreadyHit):
        timer = self.api.peekCPU(0x1497)
        if timer > 0:
            if alreadyHit == False:
                return True
            else:
                return False
        
        return False
        
    def getMarioHitTimer(self):
        timer = self.api.peekCPU(0x1497)
        return timer

    def getTile(self, dx, dy):
        x = math.floor((marioX+dx+8)/16)
        y = math.floor((marioY+dy)/16)
            
        return self.api.peekCPU(0x1C800 + math.floor(x/0x10)*0x1B0 + y*0x10 + x%0x10)


    def getSprites(self):
        sprites = {}
        for slot in range(0,11):
            status = self.api.peekCPU(0x14C8+slot)
            if status != 0:
                spritex = self.api.peekCPU(0xE4+slot) + self.api.peekCPU(0x14E0+slot)*256
                spritey = self.api.peekCPU(0xD8+slot) + self.api.peekCPU(0x14D4+slot)*256
                """  sprites[len(sprites)+1] = {"x":spritex, \
                                        "y":spritey, \
                                        "good":spritelist.Sprites[self.api.peekCPU(0x009e + slot) + 1]}
        """     
        return sprites

    def getExtendedSprites(self):
        extended = {}
        for slot in range(0,11):
            number = self.api.peekCPU(0x170B+slot)
            if number != 0:
                spritex = self.api.peekCPU(0x171F+slot) + self.api.peekCPU(0x1733+slot)*256
                spritey = self.api.peekCPU(0x1715+slot) + self.api.peekCPU(0x1729+slot)*256
                """ extended[len(extended)+1] = {"x":spritex, \
                                            "y":spritey, \
                                            "good": spritelist.extSprites[self.api.peekCPU(0x170B + slot) + 1]}
        """ 
        return extended

""" 
def getInputs():
	_M.getPositions()
	
	sprites = _M.getSprites()
	extended = _M.getExtendedSprites()
	
	local inputs = {}
	local inputDeltaDistance = {}
	
	local layer1x = self.api.peekCPU16(0x1A);
	local layer1y = self.api.peekCPU16(0x1C);
	
	
	for dy=-config.BoxRadius*16,config.BoxRadius*16,16 do
		for dx=-config.BoxRadius*16,config.BoxRadius*16,16 do
			inputs[#inputs+1] = 0
			inputDeltaDistance[#inputDeltaDistance+1] = 1
			
			tile = _M.getTile(dx, dy)
			if tile == 1 and marioY+dy < 0x1B0 then
				inputs[#inputs] = 1
			end
			
			for i = 1,#sprites do
				distx = math.abs(sprites[i]["x"] - (marioX+dx))
				disty = math.abs(sprites[i]["y"] - (marioY+dy))
				if distx <= 8 and disty <= 8 then
					inputs[#inputs] = sprites[i]["good"]
					
					local dist = math.sqrt((distx * distx) + (disty * disty))
					if dist > 8 then
						inputDeltaDistance[#inputDeltaDistance] = mathFunctions.squashDistance(dist)
						--gui.drawLine(screenX, screenY, sprites[i]["x"] - layer1x, sprites[i]["y"] - layer1y, 0x50000000)
					end
				end
			end

			for i = 1,#extended do
				distx = math.abs(extended[i]["x"] - (marioX+dx))
				disty = math.abs(extended[i]["y"] - (marioY+dy))
				if distx < 8 and disty < 8 then
					
					--console.writeline(screenX .. "," .. screenY .. " to " .. extended[i]["x"]-layer1x .. "," .. extended[i]["y"]-layer1y) 
					inputs[#inputs] = extended[i]["good"]
					local dist = math.sqrt((distx * distx) + (disty * disty))
					if dist > 8 then
						inputDeltaDistance[#inputDeltaDistance] = mathFunctions.squashDistance(dist)
						--gui.drawLine(screenX, screenY, extended[i]["x"] - layer1x, extended[i]["y"] - layer1y, 0x50000000)
					end
					--if dist > 100 then
						--dw = mathFunctions.squashDistance(dist)
						--console.writeline(dist .. " to " .. dw)
						--gui.drawLine(screenX, screenY, extended[i]["x"] - layer1x, extended[i]["y"] - layer1y, 0x50000000)
					--end
					--inputs[#inputs] = {["value"]=-1, ["dw"]=dw}
				end
			end
		end
	end
	
	return inputs, inputDeltaDistance
end
 """
""" 
def clearJoypad():
	controller = {}
	for b = 1,#config.ButtonNames do
		controller["P1 " .. config.ButtonNames[b]] = false
	end
	joypad.set(controller) """


if __name__ == "__main__":
    api = nintaco.getAPI()
    game = MarioGame(api)
