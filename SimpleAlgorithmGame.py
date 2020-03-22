from Main import Main
import csv
class SimpleAlgorithmGame(Main):
    """
    A child object of the Main game create a simple benchmark.
    """
    def __init__(self, M, S):
        """
        Initializes the part with given test parameters.
        :param M: number of tracks
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing 
        """
        super(self.M, self.S)

    def changeTrack(self):
        """
        Overrides the changeTrack() function. A simple algorithm that will just move 
        to the next higher- or lower-numbered track in case of a collision.
        """
        current_track = super.player.get_current_track()
        if current_track+1 == self.M:
            super.player.set_current_track(0)
        else:
            super.player.set_current_track(current_track+1)
        super.player.setTOnCurTrack(0)
        print(super.player)

tests = csv.reader("csv_File_With_Test_Cases_HERE")
for test in tests:
    currentGame = SimpleAlgorithmGame(test[0], test[1])
    currentGame.playGame()
    
