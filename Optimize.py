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

    def getData(self):
        return self.dataSet

    def checkConsecutive(self, alist, ele, count = 1):
        currentIndex = alist.index(ele)
        if len(alist) > currentIndex+1 and alist[currentIndex+1] == ele +1:
            return self.checkConsecutive(alist, ele+1, count+1)
        return count

    def changeTrack(self):
        """
        Overrides the changeTrack() function. A optimization algorithm will be implemented
        to decide which track to move to.
        """
        unclear = True #for the case where no best next track is found

        #sorts the safe times in each track
        for i in range(self.getNumTracks()):
            self.dataSet[i] = sorted(self.dataSet[i])

        #set base track and get the safe time on that track
        current_track = self.player.get_current_track()
        nextTrack = 0 if current_track != 0 else 1
        longestTime = 0
        if self.getTotalTime() + 1 in self.dataSet[nextTrack]:
            unclear = False
            longestTime = self.checkConsecutive(self.dataSet[nextTrack], self.getTotalTime() + 1)

        #find the safest next track
        for i in range(self.getNumTracks()):
            if i != current_track:
                if self.getTotalTime() + 1 in self.dataSet[i]:
                    unclear = False
                    currentLongest = self.checkConsecutive(self.dataSet[i], self.getTotalTime() + 1)
                    if currentLongest > longestTime:
                        longestTime = currentLongest
                        nextTrack = i
                    

        #sets the next track/ either the best or random
        if unclear == True:
            nextTrack = random.randint(0,self.getNumTracks()-1)
            while nextTrack == current_track:
                nextTrack = random.randint(0,self.getNumTracks()-1)
            self.player.set_current_track(nextTrack)
        else:
            self.player.set_current_track(nextTrack)
                    
        print(self.player)

    def checkCollision(self):
        current_track = self.player.get_current_track()
        if self.trackList[current_track].hasTrainFunc(self.current_time):
            self.player.setCollisions(self.player.getCollisions() + 1)
            return True
        else:
            if self.getTotalTime() not in self.dataSet[current_track]:
                self.dataSet[current_track].append(self.getTotalTime()) #adds safe time to data set

            return False

    def playGame(self, dataSet):
        self.dataSet = dataSet
        return super().playGame()