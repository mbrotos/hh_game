import random
import sys
class Track:
    """
    Track object .
    """
    
    def __init__(self, prob, GAME_TIME):
        """
        Construct a new 'Track' object.

        :param L0: Time it takes for a train to pass through a tunnel.
        :param L1: Time it takes for the next train to arrive.
        :return: returns nothing

        Inputs: None 
        Outputs: None
        """
        self.totalTime = GAME_TIME
        self.hasAirplane = False
        self.prob = prob
        self.rand = random.randint(1, 10)
        self.L0 = (GAME_TIME * self.prob) / self.rand
        self.L1 = (GAME_TIME * (1-self.prob)) / self.rand


    def hasTrainFunc(self, currentGameTime):
        """
        Function checks if there is a train on the tracks at the given current time
        
        :param currentGameTime: The current game time
        :return: True if there is a train on the tracks, False otherwise

        Inputs: None 
        Outputs: None
        """
        if currentGameTime % (self.L0+self.L1) > self.L1:
            return True
        else:
            return False
        
    def setLastTime(self, x):
        """
        A getter function that retuns the time since the last train on track

        :param: None
        :return: returns the time since last train

        Inputs: None 
        Outputs: None
        """
        self.lastTrainTime = x

    def getDuration(self):
        """
        A getter function that retuns the time the track will not have a train

        :param: None
        :return: returns the safe time of track

        Inputs: None 
        Outputs: None
        """
        return self.L0

    def getNextTrain(self):
        """
        A getter function that retuns the time of the next train (L1)

        :param: None
        :return: returns the time of next train

        Inputs: None 
        Outputs: None
        """
        return self.L1