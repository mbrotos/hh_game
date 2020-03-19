class Player:
    """
    Player encapsulates a hogwartz game and helping functions.
    """
    #State variables
    M = None
    L0 = None
    L1 = None
    S = None

    
    def __init__(self, M, L0, L1, S):
        """
        Construct a new 'Main' object.

        :param M: number of tracks
        :param L0: Time it takes for a train to pass through a tunnel.
        :param L1: Time it takes for the next train to arrive.
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing
        """
        self.M = M
        self.L0 = L0
        self.L1 = L1
        self.S = S

import random

#Hobo inhereits player
class Hobo(Player):
    """
    Main encapsulates a hogwartz game and helping functions.
    """
    #State variables
    messagesList = [[0,""],[1,""]] #0 meaning no varible, 1 meaning track number needed.

    
    def __init__(self, M, L0, L1, S):
        """
        Construct for a non-playing hobo.

        :param M: number of tracks
        :param L0: Time it takes for a train to pass through a tunnel.
        :param L1: Time it takes for the next train to arrive.
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing
        """
        self.M = M
        self.L0 = L0
        self.L1 = L1
        self.S = S


    def airPlaneMsg(self):
        """
        Selects a random message from the Hobo.

        :param self: the current hobo object
        :return: a string containing a message from the hobo
        """
        msgChoice = random.choice(self.messagesList)
        if (msgChoice[0]==0):
            return msgChoice[1]
        else:
            return msgChoice[1].format(super.currentTrack)
