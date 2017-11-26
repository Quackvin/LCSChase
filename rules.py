from random import randrange, seed
import playerClass, math

seed()

class LCS:
    def __init__(self):
        self.population = []
        self.matchSet = []
        self.chosenSet = []

        self.maxSize = 50
        self.pCoverWC = 0.8
        self.pMutate = 0.2

        self.accFactor = 5
        self.outcomeBinSize = 5

        self.oldDist = 0

        self.pause = False

    def run(self, enemy, player):
        if not self.pause:
            distChange = self.oldDist - enemy.getDist(player)
            print 'distance change: ', distChange
            # update parameters based on oldDist-newDist
            self.updateClassifiers(distChange)
            self.consolidateClassifiers()

            instance = enemy.createFeatureVector()

            print 'instance: ', instance

            self.matchInstance(instance)

            if len(self.matchSet) == 0:
                self.matchSet.append(self.cover(instance))

            print 'matchset length: ', len(self.matchSet)
            print 'population length: ', len(self.population)
            print 'classifiers'
            for clsfr in self.matchSet:
                print clsfr

            outcome = self.matchSetVote()

            print 'outcome', outcome
            print 'chosenset length: ', len(self.chosenSet)

            self.oldDist = enemy.getDist(player)
            self.executeOrder(enemy, outcome)


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
        xOutcome = {}
        yOutcome = {}

        for classifier in self.matchSet:
            x = str(classifier.outcome[0])
            y = str(classifier.outcome[1])

            if x in xOutcome.keys():
                xOutcome[x] += 1
            else:
                xOutcome[x] = 1
            if y in yOutcome.keys():
                yOutcome[y] += 1
            else:
                yOutcome[y] = 1

        print 'matchset votes. x:', xOutcome, 'y:', yOutcome

        max = 0
        x = ''
        for key in xOutcome:
            if xOutcome[key] > max:
                max = xOutcome[key]
                x = key
        max = 0
        y = ''
        for key in yOutcome:
            if yOutcome[key] > max:
                max = yOutcome[key]
                y = key

        x = int(x)
        y = int(y)

        unchosenSet = []
        for classifier in self.matchSet:
            if x == classifier.outcome[0] or y == classifier.outcome[1]:
                self.chosenSet.append(classifier)
            else:
                unchosenSet.append(classifier)

        self.matchSet = unchosenSet

        return [x, y]

    def executeOrder(self, enemy, outcome): #66
        enemy.increaseVel(outcome[0], outcome[1])

    def cover(self, instance):
        randomOutcome = [] # needs 2 random numbers
        randomOutcome.append(randrange(-self.accFactor, self.accFactor))
        randomOutcome.append(randrange(-self.accFactor, self.accFactor))

        newClassifier = Classifier(randomOutcome)

        for i in range(len(instance)):
            rand = float(randrange(100))/100
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

    def updateClassifiers(self, distChange):
        # update fitness
        for classifier in self.matchSet:
            classifier.matchCount += 1

        for classifier in self.chosenSet:
            classifier.matchCount += 1
            classifier.fitness += distChange

    def consolidateClassifiers(self):
        self.population.extend(self.matchSet)
        self.matchSet = []

        self.population.extend((self.chosenSet))
        self.chosenSet = []

    def printPop(self):
        for classifier in self.population:
            print classifier

    def togglePause(self):
        self.pause = not self.pause

class Classifier:
    def __init__(self, outcome):
        self.rules = []
        self.outcome = outcome
        self.binsize = 100

        self.matchCount = 0
        self.numerosity = 1
        self.fitness = 0

    def __str__(self):
        s1 = 'rules: ['
        for i in range(len(self.rules)):
            s1 += str(self.rules[i]) + ', '
        s1 = s1[:-2] + ']'
        s2 = ' outcome: [' + str(self.outcome[0]) + ', ' + str(self.outcome[1]) + ']'
        s3 = ' MC: ' + str(self.matchCount) + ' num: ' + str(self.numerosity) + ' fitness: ' + str(self.fitness)
        return s1 + s2 + s3

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