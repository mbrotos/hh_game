class Track:
    """
    Track encapsulates a hogwartz game and helping functions.
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