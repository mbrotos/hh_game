import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from SimpleAlgorithmGame import SimpleAlgorithmGame
from Optimize import Optimize

M = 5
S = 5

def optimizeGame(simpleGameObj, optimizeGameObj, dataSet = [ [] ]*M, simpleCollisionsL = [], optimizeCollisionsL = []):
    
    sCollisons = simpleGameObj.playGame()
    oCollisions = optimizeGameObj.playGame(dataSet)
    simpleCollisionsL.append(sCollisons)
    
    optimizeCollisionsL.append(oCollisions)
    dataSet = optimizeGameObj.getData()

    if oCollisions - sCollisons > 5 :
        return (simpleCollisionsL, optimizeCollisionsL)

    # Resets games without changing random probablilties 
    simpleGameObj.reset()
    optimizeGameObj.reset()

    # Recursive call
    optimizeGame(simpleGameObj, optimizeGameObj, dataSet, simpleCollisionsL, optimizeCollisionsL)
    return -1


sGame = SimpleAlgorithmGame(M,S)
oGame = Optimize(M, S, [ [] ]*M)
dataPoints = optimizeGame(sGame, oGame)
print(dataPoints[0])
print(dataPoints[1])
plt.plot(dataPoints[0])
plt.plot(dataPoints[1])
plt.ylabel('Number of Collisions')
plt.xlabel('Number of games played')
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
plt.show()