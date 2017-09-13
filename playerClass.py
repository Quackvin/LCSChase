import math

class Player:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def moveUp(self, s):
		self.y -= s
	def moveDown(self, s):
		self.y += s	
	def moveLeft(self, s):
		self.x -= s
	def moveRight(self, s):
		self.x += s

class Enemy(Player):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getDistTo(self, player):
		xdiff = self.getXDistTo(player)
		ydiff = self.getYDistTo(player)
		return math.sqrt(xdiff*xdiff + ydiff*ydiff)

	def getXDistTo(self, player):
		xdiff = self.x - player.x
		return xdiff

	def getYDistTo(self, player):
		ydiff = self.y - player.y
		return ydiff
