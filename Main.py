from Player import Player, Hobo
from Track import Track
import random
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
        if M is None:
            self.M = int(input("Input the number of tracks: "))
            self.S = int(input("Input the time that the player stays on each track before jumping to another: "))
            while self.M <= 1 or self.S <=0:
                self.M = int(input("Input the number of tracks: "))
                self.S = int(input("Input the time that the player stays on each track before jumping to another: "))

        else:
            self.M = M
            self.S = S

        self.current_time = 0
        self.trackList = [Track(self.getProb(), Main.GAME_TIME) for i in range(M)]  # creates list of tracks based on prob
        self.player = Player(100, 0) # Creates the default player with 100 health on track 1
        self.hobo = Hobo(None, None, self.M)  # creates a hobo with no health or staring and give M

    def getProb(self):
	#use probability density function to get exponential distribution.
        return expon.pdf(random.randrange(1,10))

    def getTotalTime(self):
        return self.current_time

    def reset(self):
        self.current_time = 0
        self.player.set_health(100)
        self.player.set_current_track(0)
        self.player.setCollisions(0)
        for i in range(len(self.trackList)):
            self.trackList[i].setLastTime(None)

    def getNumTracks(self):
        return self.M

    def checkCollision(self):
        current_track = self.player.get_current_track()
        if self.trackList[current_track].hasTrainFunc(self.current_time):
            self.player.setCollisions(self.player.getCollisions() + 1)
            return True
        else:
            return False

    def changeTrack(self):
        new_track = int(input("Change Tracks! You are on track {}. Pick another track to move to from 0 to {} (not including current): ".format(self.player.get_current_track(), self.M-1)))
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

            while self.player.getTOnCurTrack() < self.S:
                # Hobo airplane function call
                #self.hoboMessage()
                track = self.trackList[self.player.get_current_track()]
                # Call hasTrainFunc
                if self.checkCollision():
                    self.player.set_health(self.player.get_health() - Main.DAMAGE)
                    if self.player.get_health() <= 0:
                        break
                    self.changeTrack()

                self.player.setTOnCurTrack(self.player.getTOnCurTrack() + 1)

                self.current_time += 1

            self.changeTrack()

        if(self.player.get_health() <= 0):
            print("you dead")
        else:
            print(self.player.get_health())


        return self.player.getCollisions()



