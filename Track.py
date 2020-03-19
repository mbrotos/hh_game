import time
import random

class Track:
    """
    Track object .
    """
    
    def __init__(self):
        """
        Construct a new 'Track' object.
        :return: returns nothing
        """
        self.initTime = time.time()
        self.hasTrain = False
        self.hasAirplane = False
        self.L0 = random.randrange(1, 20)
        self.L1 = random.randrange(5, 30)

    def hasTrain(self):
        """
        :return: True if there is a train on the tracks, False otherwise
        """
        currentTime = time.time()
        if 0<=((currentTime-self.initTime)%(self.L0+self.L1))<=self.L1 :
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


