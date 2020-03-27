from Main import Main
import sys
class SimpleAlgorithmGame(Main):
    """
    A child object of the Main game that creates a simple benchmark.
    """
    def __init__(self, M, S):
        """
        Initializes the part with given test parameters.

        :param M: number of tracks
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing 

        Input: None
        Output: None
        """
        super().__init__(M, S)

    def changeTrack(self):
        """
        A function that overrides the changeTrack() function. A simple algorithm that will just move 
        to the next higher- or lower-numbered track in case of a collision.

        :param: None
        :return: None 

        Inputs: None 
        Outputs: Prints player object
        """
        current_track = self.player.get_current_track()
        if current_track+1 == self.M:
            self.player.set_current_track(0)
        else:
            self.player.set_current_track(current_track+1)
        self.player.setTOnCurTrack(0)
        print(self.player)


