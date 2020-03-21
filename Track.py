import time
import random
class Track:
    """
    Track object .
    """
    
    def __init__(self, prob, GAME_TIME):
        """
        Construct a new 'Track' object.
        :return: returns nothing
        :param L0: Time it takes for a train to pass through a tunnel.
        :param L1: Time it takes for the next train to arrive.
        """
        self.hasTrain = False
        self.hasAirplane = False
        self.prob = prob
        self.rand = random.randint(1,10)
        self.L0 = (GAME_TIME * self.prob) / self.rand
        self.L1 = (GAME_TIME * (1-self.prob)) / self.rand



    def hasTrainFunc(self, currentGameTime):
        """
        :return: True if there is a train on the tracks, False otherwise
        """
        if 0<=((currentGameTime)%(self.L0+self.L1))<=self.L1 :
            self.hasTrain = False
        else:
            self.hasTrain = True
        return self.hasTrain

    def getDuration(self):
        return self.L0

    def getNextTrain(self):
        return self.L1