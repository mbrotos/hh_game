from Main import Main
import random
class Optimize(Main):
    """
    A child object of the Main game that creates a simple benchmark.
    """
    def __init__(self, M, S, data):
        """
        Initializes the part with given test parameters.
        :param M: number of tracks
        :param S: Time that the player stays on each track before jumping to another.
        :return: returns nothing 
        """
        super().__init__(M, S)
        self.dataSet = data

    def changeTrack(self):
        """
        Overrides the changeTrack() function. A optimization algorithm will be implemented
        to decide which track to move to.
        """
        unclear = True

        for i in range(self.getNumTracks()):
            self.dataSet[i] = sorted(self.dataSet[i])

        current_track = self.player.get_current_track()
        nextTrack = 0 if current_track != 0 else 1
        longestTime = 0
        if self.getTotalTime() + 1 in self.dataSet[nextTrack]:
            count = 1
            currentIndex = self.dataSet[nextTrack].index(self.getTotalTime() + count) 
            while self.dataSet[current_track][currentIndex] == self.getTotalTime() + count + 1:
                count+=1
            if count > longestTime:
                 longestTime = count
                 unclear = False

        for i in range(self.getNumTracks()):
            if i != current_track:
                if self.getTotalTime() +1 in self.dataSet[i]:
                    count = 1
                    currentIndex = self.dataSet[nextTrack].index(self.getTotalTime() + count) 
                    while self.dataSet[i][currentIndex] == self.getTotalTime() + count + 1:
                        count+=1
                    if count > longestTime:
                        longestTime = count
                        nextTrack = i
                        unclear = False

        if unclear == True:
            self.player.set_current_track(random.randint(0,self.getNumTracks()-1))
        else:
            self.player.set_current_track(nextTrack)
                    
        #change track
        print(self.player)

    def checkCollision(self):
        current_track = self.player.get_current_track()
        if self.trackList[current_track].hasTrain:
            self.player.setCollisions(self.player.getCollisions() + 1)
            return True
        else:
            if self.getTotalTime() not in self.dataSet[current_track]:
                self.dataSet[current_track].append(self.getTotalTime()) #adds safe time to data set

            return False

    def playGame(self, dataSet):
        self.player.set_health(100)
        self.resetTime()
        self.dataSet = dataSet
        return super().playGame()