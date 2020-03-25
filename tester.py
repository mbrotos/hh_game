import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from SimpleAlgorithmGame import SimpleAlgorithmGame
from Optimize import Optimize

M = 10
S = 2

def optimizeGame(simpleGameObj, optimizeGameObj, dataSet = [ [] ]*M, simpleCollisionsL = [], optimizeCollisionsL = []):
    
    sCollisons = simpleGameObj.playGame()
    oCollisions = optimizeGameObj.playGame(dataSet)
    simpleCollisionsL.append(sCollisons)
    
    optimizeCollisionsL.append(oCollisions)
    dataSet = optimizeGameObj.getData()

    if len(optimizeCollisionsL) == 5:
        return (simpleCollisionsL, optimizeCollisionsL)
    else:
        # Resets games without changing random probablilties 
        simpleGameObj.reset()
        optimizeGameObj.reset()
        # Recursive call
        return optimizeGame(simpleGameObj, optimizeGameObj, dataSet, simpleCollisionsL, optimizeCollisionsL)


sGame = SimpleAlgorithmGame(M,S)
oGame = Optimize(M, S, [ [] ]*M)
dataPoints = optimizeGame(sGame, oGame)
plt.plot(dataPoints[0], label="Simple Algorithm")
plt.plot(dataPoints[1], label="Opptimized Algorithm")
plt.ylabel('Number of Collisions')
plt.xlabel('Number of games played')
plt.xlim(xmin=1)
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
plt.legend()
plt.show()