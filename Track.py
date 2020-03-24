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
        self.totalTime = GAME_TIME
        self.hasTrain = False
        self.hasAirplane = False
        self.prob = prob
        self.rand = random.randint(1, 10)
        self.L0 = (GAME_TIME * self.prob) / self.rand
        self.L1 = (GAME_TIME * (1-self.prob)) / self.rand
        self.lastTrainTime = None


    def hasTrainFunc(self, currentGameTime):
        """
        :return: True if there is a train on the tracks, False otherwise
        """
        # if last train time is None do probability stuff
        if self.lastTrainTime == None:
            if self.totalTime % self.rand == 0:
                self.hasTrain = True
                self.lastTrainTime = currentGameTime
            else:
                self.hasTrain = False
            return self.hasTrain

        if self.hasTrain:
            if currentGameTime - self.lastTrainTime < self.L0:
                self.hasTrain = True
            else:
                self.hasTrain = False
            return self.hasTrain
        return -1
        
    def setLastTime(self, x):
        self.lastTrainTime = x

    def getDuration(self):
        return self.L0

    def getNextTrain(self):
        return self.L1