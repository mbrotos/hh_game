from Main import Main
class Optimize(Main):
    """
    A child object of the Main game that creates a simple benchmark.
    """
    def __init__(self, M, S):
        """
        Initializes the part with given test parameters.
        :param M: number of tracks
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing 
        """
        super(self.M, self.S)
        self.current_track = None #default track before any moves are made

    def changeTrack(self):
        """
        Overrides the changeTrack() function. A optimization algorithm will be implemented
        to decide which track to move to.
        """
        self.current_track = super.player.get_current_track()
        #change track
        print(super.player)