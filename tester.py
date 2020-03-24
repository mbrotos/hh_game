import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from SimpleAlgorithmGame import SimpleAlgorithmGame
from Optimize import Optimize

M = 5
S = 5

def optimizeGame(simpleGame, optimizeGame, dataSet = [ [-1] ]*M, simpleCollisionsL = [], optimizeCollisionsL = []):
    
    oCollisions = optimizeGame.playGame(dataSet)
    simpleCollisionsL.append(simpleGame.playGame())
    
    optimizeCollisionsL.append(oCollisions)
    dataSet = optimizeGame.getData()

    if oCollisions == 0:
        return (simpleCollisionsL, optimizeCollisionsL)

    optimizeGame(simpleGame, optimizeGame, simpleCollisionsL, optimizeCollisionsL)
    return -1


sGame = SimpleAlgorithmGame(M,S)
oGame = Optimize(M, S, [ [-1] ]*M)
dataPoints = optimizeGame(sGame, oGame)
plt.plot(dataPoints[0])
plt.plot(dataPoints[1])
plt.ylabel('Number of Collisions')
plt.xlabel('Number of games played')
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
plt.show()