from Player import Player, Hobo
from Track import Track
class Main:
    """
    Main encapsulates a hogwartz game and helping functions.
    """
    GAME_TIME = 100 #WHATEVER...
    DAMAGE = 1

    def __init__(self, M=None, S=None):
        """
        Construct a new 'Main' object given all params or none.

        :param M: number of tracks
        :param L0: Time it takes for a train to pass through a tunnel.
        :param L1: Time it takes for the next train to arrive.
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing
        """
        if M is None:  # exception handling.......
            self.M = int(input("Input the number of tracks: "))
            self.S = int(input("Input the time that the player stays on each track before jumping to another: "))
        else:
            self.M = M
            self.S = S

        self.current_time = 0
        self.prob = self.getProb()  # distribution
        self.trackList = [Track(self.prob) for i in range(M)]  # creates list of tracks based on prob
        self.player = Player(100, 0) # Creates the default player with 100 health on track 1
        self.hobo = Hobo(None, None, self.M)  # creates a hobo with no health or staring and give M

        self.playGame()

    def getProb(self):
        return -1  # do something

    def checkCollision(self):
        current_track = self.player.get_current_track()
        if self.trackList[current_track].hasTrain:
            return True
        else:
            return False

    def changeTrack(self):
        new_track = int(input("Change Tracks! You are on track {}. Pick another track to move to from 1 to {} (not including current): ".format(self.player.get_current_track(), self.M)))
        while new_track == self.player.get_current_track():
            new_track = int(input("You cannot pick the same track. Pick another track: "))

        self.player.set_current_track(new_track)
        self.player.setTOnCurTrack(0)
        print(self.player)

    def hoboMessage(self):
        msg = self.hobo.airPlaneMsg()
        if msg is not None:
            print(msg)

    def playGame(self):
        
        while self.player.get_health() > 0 or self.current_time < Main.GAME_TIME:
            # play
            while self.player.getTOnCurTrack() < self.S:
                # Hobo airplane function call
                self.hoboMessage()
                track = self.trackList[self.player.get_current_track()]
                track.hasTrainFunc()
                if self.checkCollision():
                    self.player.set_health(self.player.get_health() - Main.DAMAGE)
                    if self.player.get_health() <= 0:
                        break
                    self.changeTrack()

                self.player.setTOnCurTrack += 1

            self.current_time += self.player.getTOnCurTrack()
            self.changeTrack()

        if(self.player.get_health() <= 0):
            print("you dead")
            exit(0)
        else:
            print(self.player.get_health())


