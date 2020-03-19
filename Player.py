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


#Hobo inhereits player
class Hobo(Player):
    """
    Main encapsulates a hogwartz game and helping functions.
    """

    def __init__(self, health, current_track):
        """
        Construct a new 'Main' object.

        :param health: The starting health of the player
        :param current_track: The track that the player is currently on.
        :return: returns nothing
        """
        Player.__init__(health, current_track)