<<<<<<< HEAD
import time
=======
>>>>>>> e33d64e6f5b2ad3d7acbab581833918883424c0e
import random

class Track:
    """
    Track object .
    """
    
<<<<<<< HEAD
    def __init__(self, L0, L1):
        """
        Construct a new 'Track' object.
        :return: returns nothing
        """
        self.initTime = time.time()
        self.hasTrain = False
        self.hasAirplane = False
        self.L0 = L0
        self.L1 = L1

    def hasTrain(self):
        """
        :return: True if there is a train on the tracks, False otherwise
        """
        currentTime = time.time()
        if 0<=((currentTime-self.initTime)%(self.L0+self.L1))<=self.L1 :
=======
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
        self.rand = random.randint(1, 10)
        self.L0 = (GAME_TIME * self.prob) / self.rand
        self.L1 = (GAME_TIME * (1-self.prob)) / self.rand
        self.lastTrainTime = None


    def hasTrainFunc(self, currentGameTime):
        """
        :return: True if there is a train on the tracks, False otherwise
        """
        # if last train time is None do probability stuff

        # Check if track has train

            # if True, check currentGameTime
                # check last time track had train
                    # if current game time - last time track had train is less than L0 return false
            # if False check if current game time - last time track had train is greater than or equal to L1
                #return true

        if 0<=((currentGameTime)%(self.L0+self.L1))<=self.L1 :
>>>>>>> e33d64e6f5b2ad3d7acbab581833918883424c0e
            self.hasTrain = False
        else:
            self.hasTrain = True
        return self.hasTrain

<<<<<<< HEAD
    def getAirplane(self):
        """
        :return: value of the hasAirplane variable 
        """
        return self.hasAirplane

    def setAirplane(self,value):
        """
        :param value: boolean  
        :return: nothing
        """
        self.hasAirplane = value


=======
    def getDuration(self):
        return self.L0

    def getNextTrain(self):
        return self.L1
>>>>>>> e33d64e6f5b2ad3d7acbab581833918883424c0e
