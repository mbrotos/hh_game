import time
import random
from Main import Main
class Track:
    """
    Track object .
    """
    
    def __init__(self, prob):
        """
        Construct a new 'Track' object.
        :return: returns nothing
        """
        self.hasTrain = False
        self.hasAirplane = False
        self.prob = prob
        self.rand = random.randint(1,10)
        self.L0 = (Main.GAME_TIME * self.prob) / self.rand
        self.L1 = (Main.GAME_TIME * (1-self.prob)) / self.rand



    def hasTrainFunc(self):
        """
        :return: True if there is a train on the tracks, False otherwise
        """
        currentTime = time.time()
        if 0<=((currentTime)%(self.L0+self.L1))<=self.L1 :
            self.hasTrain = False
        else:
            self.hasTrain = True
        return self.hasTrain

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
