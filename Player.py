class Player:
    """
    Player encapsulates a hogwartz game and helping functions.
    """
    
    def __init__(self, health, current_track):
        """
        Construct a new 'Main' object.

        :param health: The starting health of the player
        :param current_track: The track that the player is currently on.
        :return: returns nothing
        """
        self.health = health
        self.current_track = current_track

    def get_health(self):
        return self.health

    def get_current_track(self):
        return self.current_track

    def set_current_track(self, track):
        self.current_track = track

    def set_health(self, new_health):
        self.health = new_health

    def __str__(self):
        return "Player is on track: {} and has {} health. ".format(self.current_track, self.health)

#Hobo inhereits player
class Hobo:
    """
    Main encapsulates a hogwartz game and helping functions.
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