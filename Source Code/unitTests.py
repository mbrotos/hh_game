import HtmlTestRunner
import unittest
import random
from Main import *

class TestGame(unittest.TestCase): 
      
    """
    Main.py test cases.
    """

    def test_getProb(self): 
        """
        Test the random generation of a probablilty distribution for a given game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertIsInstance(testGame.prob, float)

    def test_getTotalTime(self):
        """
        Test the total time getter for a given game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(0, testGame.getTotalTime())

    def test_reset(self):
        """
        Test the reset function for a given game which will be used in the optimization.
        The probablity distribution is also tested to be sure it is kept the same.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        previousProb = testGame.prob
        testGame.reset()
        self.assertEqual(0, testGame.getTotalTime())
        self.assertEqual(100, testGame.player.get_health())
        self.assertEqual(0, testGame.player.get_current_track())
        self.assertEqual(0, testGame.player.getTOnCurTrack())
        self.assertEqual(0, testGame.player.getCollisions())
        self.assertEqual(previousProb, testGame.prob)

    def test_getNumTracks(self):
        """
        Tests the number of track getter for a given game.
        """
        num = random.randrange(2,100)
        testGame = Main(num, random.randrange(1,5))
        self.assertEqual(num, testGame.getNumTracks())
        
    """
    Player.py test cases.
    """
    def test_get_health(self):
        """
        Tests the player health getter for a given starting game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(100, testGame.player.get_health())
    
    def test_get_curret_track(self):
        """
        Tests the player current track getter for a given starting game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(0, testGame.player.get_current_track())
    
    def test_set_health(self):
        """
        Tests the player health setter for a given game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        testGame.player.set_health(50)
        self.assertEqual(50, testGame.player.health)

    def test_getTOnCurTrack(self):
        """
        Tests the player time on current track getter for a given starting game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(0, testGame.player.getTOnCurTrack())

    def test_setTOnCurTrack(self):
        """
        Tests the players time on current track setter.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        testGame.player.setTOnCurTrack(50)
        self.assertEqual(50,testGame.player.getTOnCurTrack())

    def test_getCollisions(self):
        """
        Tests the player collisions getter for a given starting game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(0, testGame.player.getCollisions())

    def test_setCollisions(self):
        """
        Tests the player collisions setter for a given game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        testGame.player.setCollisions(50)
        self.assertEqual(50, testGame.player.getCollisions())

    """
    Test for hobo class.
    """
    def test_get_hobo_health(self):
        """
        Tests the hobo health getter for a given starting game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(100, testGame.hobo.get_health())
    
    def test_get_curret_hobo_track(self):
        """
        Tests the hobo current track getter for a given starting game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(0, testGame.hobo.get_current_track())
    
    def test_set_hobo_health(self):
        """
        Tests the hobo health setter for a given game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        testGame.hobo.set_health(50)
        self.assertEqual(50, testGame.hobo.health)

    def test_getTOnCurTrack_hobo(self):
        """
        Tests the hobo time on current track getter for a given starting game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(0, testGame.player.getTOnCurTrack())

    def test_setTOnCurTrack_hobo(self):
        """
        Tests the hobo time on current track setter.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        testGame.hobo.setTOnCurTrack(50)
        self.assertEqual(50,testGame.hobo.getTOnCurTrack())

    def test_getCollisions_hobo(self):
        """
        Tests the hobo collisions getter for a given starting game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        self.assertEqual(0, testGame.hobo.getCollisions())

    def test_setCollisions_hobo(self):
        """
        Tests the hobo collisions setter for a given game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        testGame.hobo.setCollisions(50)
        self.assertEqual(50, testGame.hobo.getCollisions())

    """
    Track.py test cases.
    """

    def test_hasTrainFunc(self):
        """
        Tests a has train function for  given track for a given game.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        time = testGame.getTotalTime()
        self.assertIsInstance(testGame.trackList[0].hasTrainFunc(time), bool)

    def test_setLastTime(self):
        """
        Tests a given tracks last collision time for a given track
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        testGame.trackList[0].setLastTime(20)
        self.assertEqual(20, testGame.trackList[0].lastTrainTime)

    def test_getDuration(self):
        """
        Tests a duration getter for a given track.
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        rand = testGame.trackList[0].rand
        L0Test = (Main.GAME_TIME* testGame.prob)/rand
        self.assertEqual(L0Test, testGame.trackList[0].getDuration())

    def test_getNextTrain(self):
        """
        Tests the time untill next train for a given track
        """
        testGame = Main(random.randrange(2,100),random.randrange(1,5))
        rand = testGame.trackList[0].rand
        L1Test = (Main.GAME_TIME* (1-testGame.prob))/rand
        self.assertEqual(L1Test, testGame.trackList[0].getNextTrain())

if __name__ == '__main__': 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\adams\\OneDrive\\OneDrive - Ryerson University\\Documents\\School\\Year 2\\CPS406\\hh_game'))