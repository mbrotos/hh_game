import random
from Player import Player, Hobo
from Track import Track
from scipy.stats import expon
import sys

class Main:
    """
    Main encapsulates a hogwartz game and helping functions.
    """
    GAME_TIME = 100
    DAMAGE = 1

    def __init__(self, M=None, S=None):
        """
        Construct a new 'Main' object given all params or none.

        :param M: number of tracks
        :param L0: Time it takes for a train to pass through a tunnel.
        :param L1: Time it takes for the next train to arrive.
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing

        Inputs: M and S values if none were given in params
        Output: None
        """
        if M is None:
            try:
                self.M = int(input("Input the number of tracks: "))
                self.M = int(input("Input the time that the player stays on each track before jumping to another: "))
                while self.M <= 1 or self.M <=0:
                    self.M = int(input("Incorrect. Input the number of tracks: "))
                    self.M = int(input("Incorrect. Input the time that the player stays on each track before jumping to another: "))
            except:
                print("Your input was invalid!")
        else:
            self.M = M
            self.S = S

        self.current_time = 0
        self.prob = self.getProb()
        self.trackList = [Track(self.prob, Main.GAME_TIME) for i in range(self.M)]  # creates list of tracks based on prob
        self.player = Player(100, 0) # Creates the default player with 100 health on track 1
        self.hobo = Hobo(None, None, self.M)  # creates a hobo with no health or staring and give M

    def getProb(self):
        """
        Function to get probability distribution for track. It uses probability density function to get exponential distribution.

        :param None
        :return: returns the probability value of track

        Inputs: None 
        Outputs: None
        """
        return expon.pdf(random.randrange(1,5)/7.0)

    def getTotalTime(self):
        """
        Function to get current game time

        :param None
        :return: returns the total currnt game time played

        Inputs: None 
        Outputs: None
        """
        return self.current_time

    def reset(self):
        """
        Function to reset the game play without changing all the random variables of track info (valuse like L1 and L0 stay the same)

        :param None
        :return: None

        Inputs: None 
        Outputs: None
        """
        self.current_time = 0
        self.player.set_health(100)
        self.player.set_current_track(0)
        self.player.setTOnCurTrack(0)
        self.player.setCollisions(0)

    def getNumTracks(self):
        """
        Function to get the total amount of tracks in the game

        :param None
        :return: returns M value, which is the total amount of tracks for game

        Inputs: None 
        Outputs: None
        """
        return self.M

    def checkCollision(self):
        """
        Function to check if the player has collided with a train on the track at the given time

        :param None
        :return: returns True if user has collided with a train on the given track, False if no collision at current time

        Inputs: None 
        Outputs: None
        """
        current_track = self.player.get_current_track()
        if self.trackList[current_track].hasTrainFunc(self.current_time):
            self.player.setCollisions(self.player.getCollisions() + 1)
            return True
        else:
            return False

    def changeTrack(self):
        """
        Function to get input from user for a change of track. Prompts user for a new track number. Handles case with same track number input and promts user again for new track number.
        Sets current track instance variable to user input and time on new track to 0

        :param None
        :return: None

        Inputs: New track number 
        Outputs: prints player ojbect
        """
        new_track = int(input("Change Tracks! You are on track {}. Pick another track to move to from 0 to {} (not including current): ".format(self.player.get_current_track(), self.M-1)))
        while new_track == self.player.get_current_track():
            new_track = int(input("You cannot pick the same track. Pick another track: "))
        self.player.set_current_track(new_track)
        self.player.setTOnCurTrack(0)
        print(self.player)

    def hoboMessage(self):
        """
        Function gets message from HOBO Message options and prints hobo message to consle

        :param None
        :return: None

        Inputs: None 
        Outputs: print hobo message
        """
        msg = self.hobo.airPlaneMsg()
        if msg is not None:
            print(msg)

    def playGame(self):
        """
        Function assembeles all functions to create the overall game play.
        The while loops runs for every iteration of one game-time second (time unit).
        Outputs when player is dead or game time is reached

        :param None
        :return: None

        Inputs: None 
        Outputs: Prints End Game results (You win or You lose)
        """        
        while self.player.get_health() > 0 and self.current_time < Main.GAME_TIME:

            while self.player.getTOnCurTrack() < self.S and self.current_time < Main.GAME_TIME:
                self.hoboMessage()
                if self.checkCollision():
                    self.player.set_health(self.player.get_health() - Main.DAMAGE)
                    if self.player.get_health() <= 0:
                        break
                    self.changeTrack()

                self.player.setTOnCurTrack(0)

                self.current_time += 1

            if self.current_time >= Main.GAME_TIME:
                break

            self.changeTrack()

        if(self.player.get_health() <= 0):
            print("you dead")
        else:
            print(self.player.get_health())


        return self.player.getCollisions()


if __name__ == "__main__":
    game = Main()
    game.playGame()

