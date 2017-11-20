from random import randrange, seed
import playerClass, math

seed()

class LCS:
    def __init__(self):
        self.population = []
        self.matchSet = []
        self.correctSet = []
        self.maxSize = 50

    def matchInstance(self, enemy):
        instance = enemy.createFeatureVector()
        incorrectSet = []
        for classifier in self.population:
            if self.isMatching(classifier, instance):
                self.matchSet.append(classifier)
            else:
                incorrectSet.append(classifier)
        self.population = incorrectSet

        if len(self.matchSet) == 0:
            self.matchSet.append(self.cover(instance))

    def isMatching(self, classifier, instance):
        return True

    def matchSetVote(self):
        pass

    def executeOrder(self, enemy): #66
        pass

    def cover(self, instance):
        pass

    def GA(self):
        pass

class classifier:
    def __init__(self, outcome):
        self.rules = []
        self.outcome = outcome
        self.binsize = 10


def valueToBin(val, binSize):
    return int(math.floor(val/binSize))