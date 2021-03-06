import math
import numpy as np


class Player(object):
	def __init__(self, x, y):
		self.pos = np.array([float(x),float(y)])
		self.vel = np.array([0.0,0.0])
		self.size = 10
		self.maxVel = 10

	def move(self, maxX, maxY):
		if self.pos[0] + self.vel[0] + self.size > maxX:
			self.pos[0] = maxX - self.size
			self.vel[0] = 0
		elif self.pos[0] + self.vel[0] < 0:
			self.pos[0] = 0
			self.vel[0] = 0
		else:
			self.pos[0] = self.pos[0] + self.vel[0]

		if self.pos[1] + self.vel[1] + self.size > maxY:
			self.pos[1] = maxY - self.size
			self.vel[1] = 0
		elif self.pos[1] + self.vel[1] < 0:
			self.pos[1] = 0
			self.vel[1] = 0
		else:
			self.pos[1] = self.pos[1] + self.vel[1]


	def increaseVel(self, x, y):
		self.vel = self.vel + [x,y]
		if self.vel[0] > self.maxVel:
			self.vel[0] = self.maxVel
		if self.vel[1] > self.maxVel:
			self.vel[1] = self.maxVel
	def setXVel(self, x):
		self.vel[0] = x

	def setYVel(self, y):
		self.vel[1] = y

	def draw(self, pygame, screen):
		pygame.draw.rect(screen, (255, 255, 255), (self.pos[0], self.pos[1], self.size, self.size))



class Enemy(Player, object):
	def __init__(self, x, y, player, mapW, mapH):
		super(Enemy, self).__init__(x, y)
		self.pos = np.array([float(x), float(y)])
		self.vel = np.array([0, 0])
		self.size = 10
		self.target = player

		self.mapW = mapW
		self.mapH = mapH

	def getRelPosOf(self, target):
		xdiff = self.getXDistTo(target)
		ydiff = self.getYDistTo(target)
		return [xdiff, ydiff]

	def getXDistTo(self, target):
		xdiff = target.pos[0] - self.pos[0]
		return xdiff

	def getYDistTo(self, target):
		ydiff = target.pos[1] - self.pos[1]
		return ydiff

	def getRelVelOf(self, target):
		return target.vel - self.vel

	def createFeatureVector(self):
		fv = []
		fv.extend(self.getRelPosOf(self.target))
		fv.extend(self.getRelVelOf(self.target))
		# # closeness to right wall
		# fv.append(self.mapW - self.pos[0])
		# # closeness to left wall
		# fv.append(self.pos[0])
		# # closeness to bottom wall
		# fv.append(self.mapH - self.pos[1])
		# # closeness to top wall
		# fv.append(self.pos[1])

		return fv

	def getDist(self, target):
		xdiff = float(self.getXDistTo(target))
		ydiff = float(self.getYDistTo(target))

		return math.sqrt(xdiff**2 + ydiff**2)

	def draw(self, pygame, screen):
		pygame.draw.rect(screen, (0, 0, 0), (self.pos[0], self.pos[1], self.size, self.size))
