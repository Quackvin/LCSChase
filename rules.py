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

    def matchRules(self, xDist, yDist):
        matched = []

        for rule in self.rules:
            xMatch = False
            yMatch = False
            if (rule.xop == -1 and xDist < rule.xs) or \
                    (rule.xop == 0 and xDist == rule.xs) or \
                    (rule.xop == 1 and xDist > rule.xs):
                xMatch = True
            if (rule.yop == -1 and yDist < rule.ys) or \
                    (rule.yop == 0 and yDist == rule.ys) or \
                    (rule.yop == 1 and yDist > rule.ys):
                yMatch = True
            if xMatch and yMatch:
                matched.append(rule)
        return matched

    def rulesVote(self, matchSet):
        # [x, y]
        vec = [0, 0]
        for rule in matchSet:
            if rule.outVal < 0:
                vec[rule.outAxis] -= 1
            else:
                vec[rule.outAxis] += 1

        return vec

    def actionRules(self, player, enemy, maxX, maxY):
        xDist = enemy.getXDistTo(player)
        yDist = enemy.getYDistTo(player)
        dist = enemy.getDistTo(player)

        matchSet = self.matchRules(xDist, yDist)
        actionVec = self.rulesVote(matchSet)
        print(actionVec)
        # add movements
        if actionVec[0] < 0:
            print('move left')
            enemy.moveH(-10, maxX)
        elif actionVec[0] > 0:
            print('move right')
            enemy.moveH(10, maxX)
        if actionVec[1] < 0:
            print('move down')
            enemy.moveV(-10, maxY)
        elif actionVec[1] > 0:
            print('move up')
            enemy.moveV(10, maxY)

        for rule in matchSet:
            print('out axis:', rule.outAxis, 'action vector:', actionVec, 'out val:', rule.outVal)
            if rule.outAxis == 0 and (actionVec[0] < 0 and rule.outVal == -1) or (
                            actionVec[0] > 0 and rule.outVal == 1) or \
                                    rule.outAxis == 1 and (actionVec[1] < 0 and rule.outVal == -1) or (
                            actionVec[1] > 0 and rule.outVal == 1) or \
                            rule.outVal == 0:
                if enemy.getDistTo(player) < dist:
                    print('fitness up')
                    rule.fitness += 1
                else:
                    print('fitness down')
                    rule.fitness -= 1

        if len(matchSet) == 0:
            print('no matches')
            self.remove(0.7)
            self.GA()
        else:
            fitnesses = [rule.fitness for rule in self.rules]
            print("fitnesses", fitnesses, '\n')

    def GA(self):
        randIndex = randrange(1, len(self.rules))
        # dont breed over limit
        if len(self.rules) <= self.limit:
            rule1 = self.rules[randIndex]
            if rule1.fitness >= 0 and 1 / (randIndex + rule1.fitness) < self.pMutate:
                self.rules.append(rule1.mutate(self.pMutate))
                # print len(self.rules)
        randIndex1 = randrange(1, len(self.rules))
        randIndex2 = randrange(1, len(self.rules))
        if len(self.rules) <= self.limit:
            rule2 = self.rules[randIndex1]
            rule3 = self.rules[randIndex2]
            if rule2.fitness >= 0 and 1 / (randIndex1 + rule2.fitness) < self.pCross:
                self.rules.append(rule2.crossover(rule3))
                # print len(self.rules)

    def remove(self, p):
        # self.rules = [rule for rule in self.rules if rule.fitness >= 0]
        # self.rules = [rule for rule in self.rules if (float(rule.fitness)/(randrange(1,10))) > 0.1]
        tempRules = []
        for rule in self.rules:
            i = randrange(1, 10)
            survivalThesh = p
            if float(rule.fitness) / i > survivalThesh:
                tempRules.append(rule)
            else:
                print('rule deleted')
        self.rules = tempRules

        if len(self.rules) <= 1:
            print('low pop')
            self.createRule()
            self.createRule()


class Rule:
    # make more flexible for rules with more features
    # add output
    def __init__(self, xs=None, ys=None, xop=None, yop=None, outAxis=None, outVal=None, fitness=None):
        self.xs = randrange(0, 300) if xs == None else xs
        self.ys = randrange(0, 300) if ys == None else ys
        # -1:<, 0:==, 1:>
        self.xop = randrange(-1, 2) if xop == None else xop
        self.yop = randrange(-1, 2) if yop == None else yop

        # 0 for x, 1 for y
        self.outAxis = randrange(0, 2) if outAxis == None else outAxis
        self.outVal = randrange(-1, 2) if outVal == None else outVal

        self.fitness = 1 if fitness == None else fitness

    # print "new rule:", self.xs, self.ys, self.xop, self.yop, self.outAxis, self.outVal
    # print 'x', '<' if self.xop==-1 else '==' if self.xop == 0 else '>', self.xs, \
    # 	'y', '<' if self.yop==-1 else '==' if self.yop == 0 else '>', self.ys, \
    # 	'| out~ dir:', 'x' if self.outAxis == 0 else 'y', 'val:', self.outVal

    # p is probability of mutation
    def mutate(self, p):
        r = randrange(0, int(6 / p))
        xs = self.xs if r != 0 else self.xs + 1 if randrange(0, 2) == 1 else self.xs - 1
        ys = self.ys if r != 1 else self.ys + 1 if randrange(0, 2) == 1 else self.ys - 1
        xop = self.xop if r != 2 else randrange(-1, 2)
        yop = self.yop if r != 3 else randrange(-1, 2)
        outAxis = self.outAxis if r != 4 else randrange(0, 2)
        outVal = self.outVal if r != 5 else randrange(0, 2)

        # print 'mutate'
        return Rule(xs, ys, xop, yop, outAxis, outVal, self.fitness)

    def crossover(self, partner):
        # 0 takes from self, 1 takes from partner
        xsParent = randrange(0, 2)
        ysParent = randrange(0, 2)
        xopParent = randrange(0, 2)
        yopParent = randrange(0, 2)
        outAParent = randrange(0, 2)
        outVParent = randrange(0, 2)

        xs = self.xs if xsParent == 0 else partner.xs
        ys = self.ys if ysParent == 0 else partner.ys
        xop = self.xop if xopParent == 0 else partner.xop
        yop = self.yop if yopParent == 0 else partner.yop
        outAxis = self.outAxis if outAParent == 0 else partner.outAxis
        outVal = self.outVal if outVParent == 0 else partner.outVal

        # print 'cross over'
        return Rule(xs, ys, xop, yop, outAxis, outVal, self.fitness)
