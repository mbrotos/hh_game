import random
from Main import Main
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



#Hobo inhereits player
class Hobo(Player):
    """
    Main encapsulates a hogwartz game and helping functions.
    """
    #State variables
    messagesList = ["",""] 

    
    def __init__(self, health = None, current_track = None):
        """
        Construct for a hobo, whether player or non-player(default non-player).

        :param health: The starting health of the player
        :param current_track: The track that the player is currently on.
        :return: returns nothing
        """
        super(health, current_track)



    def airPlaneMsg(self):
        """
        Selects a random message from the Hobo.

        :return: a string containing a message from the hobo
        """
        return (random.choice(self.messagesList)).format(random.randint(1,Main.M))
        
