from SimpleAlgorithmGame import SimpleAlgorithmGame
from Optimize import Optimize

tests = [] #get test cases somehow
for test in tests:
    currentSimpleGame = SimpleAlgorithmGame(test[0], test[1])
    currentOptimizedGame = Optimize(test[0], test[1])
    
    currentSimpleGame.playGame()#catch some return values to plot
    currentOptimizedGame.playGame()# ''

    