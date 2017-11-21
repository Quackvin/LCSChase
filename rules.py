from random import randrange, seed
import playerClass, math

seed()

class LCS:
    def __init__(self):
        self.population = []
        self.matchSet = []
        self.correctSet = []

        self.maxSize = 50
        self.pCover = 0.5
        self.pMutate = 0.2

    def run(self, enemy, player):
        instance = enemy.createFeatureVector()

        self.matchInstance(instance)

        if len(self.matchSet) == 0:
            self.matchSet.append(self.cover(instance))

        outcome = self.matchSetVote()

        oldDistance = enemy.getDist(player)
        self.executeOrder(enemy, outcome)
        newDistance = enemy.getDist(player)

        # update parameters based on oldDist-newDist


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
        pass

    def executeOrder(self, enemy, outcome): #66
        pass

    def cover(self, instance):
        randomOutcome = [] # needs 2 random numbers
        newClassifier = classifier(randomOutcome)

        for i in range(len(instance)):
            # randomly add # otherwise add instance[i]
            pass
        self.matchSet.append(newClassifier)

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
        pass

class classifier:
    def __init__(self, outcome):
        self.rules = []
        self.outcome = outcome
        self.binsize = 10

    def addRule(self, value):
        if value == '#':
            self.rules.append('#')
        else:
            self.rules.append(valueToBin(value, self.binsize))

    def checkRule(self, i, instVal):
        if self.rules[i] == '#' or self.rules[i] == valueToBin(instVal):
            return True
        return False


def valueToBin(val, binSize):
    return int(math.floor(val/binSize))