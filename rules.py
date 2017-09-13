from random import randrange, seed
import playerClass

seed()

class Ruleset:
	def __init__(self, limit, pMutate, pCross):
		self.rules = []
		self.limit = limit
		self.pMutate = pMutate
		self.pCross = pCross

	def createRule(self):
		if len(self.rules) <= self.limit:
			self.rules.append(Rule())

	def initiliseSet(self):
		self.createRule()
		self.createRule()
		self.createRule()
		self.createRule()

	def actionRules(self, player, enemy):
		for rule in self.rules:
			xDist = enemy.getXDistTo(player)
			yDist = enemy.getYDistTo(player)
			dist = enemy.getDistTo(player)

			if rule.xop == -1 and xDist < rule.xs:
				if rule.outAxis == 0:
					enemy.moveLeft(rule.outVal)
				else:
					enemy.moveRight(rule.outVal)
			if rule.xop == 0 and xDist == rule.xs:
				if rule.outAxis == 0:
					enemy.moveLeft(rule.outVal)
				else:
					enemy.moveRight(rule.outVal)
			if rule.xop == 1 and xDist > rule.xs:
				if rule.outAxis == 0:
					enemy.moveLeft(rule.outVal)
				else:
					enemy.moveRight(rule.outVal)

			if rule.yop == -1 and yDist < rule.ys:
				if rule.outAxis == 0:
					enemy.moveUp(rule.outVal)
				else:
					enemy.moveDown(rule.outVal)
			if rule.yop == 0 and yDist == rule.ys:
				if rule.outAxis == 0:
					enemy.moveUp(rule.outVal)
				else:
					enemy.moveDown(rule.outVal)
			if rule.yop == 1 and yDist > rule.ys:
				if rule.outAxis == 0:
					enemy.moveUp(rule.outVal)
				else:
					enemy.moveDown(rule.outVal)

			if enemy.getDistTo(player) > dist:
				rule.fitness += 5
			else:
				rule.fitness -= 1
			if rule.fitness <= 0:
				rule.fitness = 1

	def GA(self):
		randIndex = randrange(1,len(self.rules))
		if len(self.rules) <= self.limit:
			rule1 = self.rules[randIndex]
			if 1/(rule1.fitness) < self.pMutate:
				self.rules.append(rule1.mutate(self.pMutate))
		randIndex1 = randrange(1,len(self.rules))
		randIndex2 = randrange(1,len(self.rules))
		if len(self.rules) <= self.limit:
			rule2 = self.rules[randIndex1]
			rule3 = self.rules[randIndex2]
			if 1/(rule2.fitness) < self.pCross:
				self.rules.append(rule2.crossover(rule3))

	def remove(self):
		for i in xrange(0,len(self.rules)):
			rule = self.rules[i]
			randIndex = randrange(0,100)
			if rule.fitness * 1/(randIndex+1) < 0.2:
				self.rules.pop(i)

class Rule:
	# make more flexible for rules with more features
	# add output
	def __init__(self, xs=None, ys=None, xop=None, yop=None, outAxis=None, outVal=None):
		self.xs = randrange(0,300) if xs == None else xs
		self.ys = randrange(0,300) if ys == None else ys
		# -1:<, 0:==, 1:>
		self.xop = randrange(-1,2) if xop == None else xop
		self.yop = randrange(-1,2) if yop == None else yop

		self.outAxis = randrange(0,2) if outAxis == None else outAxis
		self.outVal = randrange(0,2) if outVal == None else outVal

		self.fitness = 1

	# p is probability of mutation
	def mutate(self, p):
		r = randrange(0,int(6/p))
		xs = self.xs if r != 0 else self.xs+1 if randrange(0,2)==1 else self.xs-1
		ys = self.ys if r != 1 else self.ys+1 if randrange(0,2)==1 else self.ys-1
		xop = self.xop if r != 2 else randrange(-1,2)
		yop = self.yop if r != 3 else randrange(-1,2)
		outAxis = self.outAxis if r != 4 else randrange(0,2)
		outVal = self.outVal if r != 5 else randrange(0,2)

		return Rule(xs,ys,xop,yop,outAxis,outVal)

	def crossover(self, partner):
		# 0 takes from self, 1 takes from partner
		xsParent = randrange(0,2)
		ysParent = randrange(0,2)
		xopParent = randrange(0,2)
		yopParent = randrange(0,2)
		outAParent = randrange(0,2)
		outVParent = randrange(0,2)

		xs = self.xs if xsParent == 0 else partner.xs
		ys = self.ys if ysParent == 0 else partner.ys
		xop = self.xop if xopParent == 0 else partner.xop
		yop = self.yop if yopParent == 0 else partner.yop
		outAxis = self.outAxis if outAParent == 0 else partner.outAxis
		outVal = self.outVal if outVParent == 0 else partner.outVal

		return Rule(xs,ys,xop,yop,outAxis,outVal)

