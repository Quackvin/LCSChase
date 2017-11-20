import math
import numpy as np


class Player(object):
	def __init__(self, x, y):
		self.pos = np.array([float(x),float(y)])
		self.vel = np.array([0.0,0.0])
		self.size = 10
		self.maxVel = 10

	def move(self, maxX, maxY):
		self.pos = self.pos + self.vel
		if self.pos[1] > maxY:
			self.pos[1] = maxY - self.size
		elif self.pos[1] < 0:
			self.pos[1] = 0
		if self.pos[0] > maxX:
			self.pos[0] = maxX - self.size
		elif self.pos[0] < 0:
			self.pos[0] = 0

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
	def __init__(self, x, y, player):
		super(Enemy, self).__init__(x, y)
		self.pos = np.array([float(x), float(y)])
		self.vel = np.array([0, 0])
		self.size = 10
		self.target = player

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