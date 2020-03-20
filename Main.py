from Player import Player, Hobo
from Track import Track
class Main:
    """
    Main encapsulates a hogwartz game and helping functions.
    """
    GAME_TIME = 100 #WHATEVER...

    def __init__(self, M=None, S=None):
        """
        Construct a new 'Main' object given all params or none.

        :param M: number of tracks
        :param L0: Time it takes for a train to pass through a tunnel.
        :param L1: Time it takes for the next train to arrive.
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing
        """
        if(M==None):#exception handling.......
            self.M = int(input("Input the number of tracks: "))
            self.S = int(input("Input the time that the player stays on each track before jumping to another: "))
        else:
            self.M = M
            self.S = S

        self.current_time = 0
        self.prob = self.getProb() #distribution
        self.trackList = [Track(self.prob) for i in range(M)] #creates list of tracks based on prob
        self.player = Player(100, self.trackList[0]) #Creates the default player with 100 health on track 1
        self.hobo = Hobo(None, None, self.M) #creates a hobo with no health or staring and give M

        self.playGame()

    def getProb(self):
        return -1#do something

    def playGame(self):
        
        while(self.player.get_health() > 0 or self.current_time < Main.GAME_TIME):
            #play
            while(self.player.getTOnCurTrack() < self.S ):#or when he/she gets hit
                #check if hit
                    #set health and change track if alive

                self.player.setTOnCurTrack += 1

            self.current_time += self.player.getTOnCurTrack()

        if(self.player.get_health() <= 0):
            print("you dead")
            exit(0)
        else:
            print(self.player.get_health())


    

    
