import math

class Player(object):
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def moveV(self, s, maxY):
		self.y -= s
		if self.y > maxY:
			self.y = maxY - 10
		elif self.y < 0:
			self.y = 0

	def moveH(self, s, maxX):
		self.x += s
		if self.x > maxX:
			self.x = maxX - 10
		elif self.x < 0:
			self.x = 0

class Enemy(Player, object):
	def __init__(self, x, y):
		super(Enemy,self).__init__(x,y)
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
