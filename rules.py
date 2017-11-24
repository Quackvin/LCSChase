from random import randrange, seed
import playerClass, math

seed()

class LCS:
    def __init__(self):
        self.population = []
        self.matchSet = []
        self.correctSet = []

        self.maxSize = 50
        self.pCoverWC = 0.5
        self.pMutate = 0.2

        self.accFactor = 2
        self.outcomeBinSize = 5

    def run(self, enemy, player):
        instance = enemy.createFeatureVector()

        print 'instance: ', instance

        self.matchInstance(instance)

        if len(self.matchSet) == 0:
            self.matchSet.append(self.cover(instance))

        print 'matchset length: ', len(self.matchSet)
        print 'population length: ', len(self.population)
        # print 'classifiers'
        # for i in range(len(self.matchSet)):
        #     print 'rules:', self.matchSet[i].rules, 'outcome:',self.matchSet[i].outcome

        outcome = self.matchSetVote()

        print 'outcome', outcome

        oldDistance = enemy.getDist(player)
        self.executeOrder(enemy, outcome)
        newDistance = enemy.getDist(player)

        # update parameters based on oldDist-newDist

        self.consolidateClassifiers()

        print ''

    def matchInstance(self, instance):
        incorrectSet = []
        for classifier in self.population:
            if self.isMatching(classifier, instance):
                self.matchSet.append(classifier)
            else:
                incorrectSet.append(classifier)
        self.population = incorrectSet

    def isMatching(self, classifier, instance):
        for i in range(len(instance)):
            if not classifier.checkRule(i, instance[i]):
                return False
        return True

    def matchSetVote(self):
        xOutcome = [0 for i in range(self.outcomeBinSize)]
        yOutcome = [0 for i in range(self.outcomeBinSize)]

        for classifier in self.matchSet:
            x = classifier.outcome[0]
            y = classifier.outcome[1]

            x = int(x * self.outcomeBinSize / self.accFactor)
            y = int(y * self.outcomeBinSize / self.accFactor)

            xOutcome[x] += 1
            yOutcome[y] += 1

        print 'matchset vote. x:', xOutcome, 'y:', yOutcome

        return [float(max(xOutcome))*self.accFactor/self.outcomeBinSize, float(max(yOutcome))*self.accFactor/self.outcomeBinSize]

    def executeOrder(self, enemy, outcome): #66
        enemy.increaseVel(outcome[0], outcome[1])

    def cover(self, instance):
        randomOutcome = [] # needs 2 random numbers

        # use valtobin

        newClassifier = Classifier(randomOutcome)

        for i in range(len(instance)):
            rand = randrange(100)/100
            if rand > self.pCoverWC:
                newClassifier.addRule('#')
            else:
                newClassifier.addRule(instance[i])

        return newClassifier

    def GA(self):
        pass

    def chooseParents(self):
        pass

    def crossover(self):
        pass

    def mutate(self):
        pass

    def enforceSize(self):
        pass

    def subsume(self):
        pass

    def updateClassifier(self):
        pass

    def consolidateClassifiers(self):
        self.population.extend(self.matchSet)
        self.matchSet = []

class Classifier:
    def __init__(self, outcome):
        self.rules = []
        self.outcome = outcome
        self.binsize = 10

        self.numerosity = 1
        self.accuracy = 0
        self.fitness = 0

    def addRule(self, value):
        if value == '#':
            self.rules.append('#')
        else:
            self.rules.append(valueToBin(value, self.binsize))

    def checkRule(self, i, instVal):
        if self.rules[i] == '#' or self.rules[i] == valueToBin(instVal, self.binsize):
            return True
        return False


def valueToBin(val, binSize):
    return int(math.floor(val/binSize))