# -*- coding: utf-8 -*- 
import sys, os
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from SimpleAlgorithmGame import SimpleAlgorithmGame
from Optimize import Optimize


def blockPrint():
    """
    Disables output to stdout.

    :param: None
    :return: returns nothing
    """
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    """
    Enables output to stdout.

    :param: None
    :return: returns nothing
    """
    sys.stdout = sys.__stdout__


def optimizeGame(simpleGameObj, optimizeGameObj, dataSet, simpleCollisionsL = [], optimizeCollisionsL = []):
    """
    Runs both optimized and simple game alogirthms storing number of collision, recursively.

    :param simpleGameObj: an instance of the game running the simple algorithm.
    :param optimizeGameObj: an instance of the game running the optimized algorithm.
    :param dataSet: The running dataset maintained between optimized game runs.
    :param simpleCollisionsL: The runnning list of collosions per simple game.
    :param optimizeCollisionsL: The runnning list of collosions per optimized game.
    :return (simpleCollisionsL, optimizeCollisionsL): returns tuple containing list of number of collisions.
    """
    sCollisons = simpleGameObj.playGame()
    oCollisions = optimizeGameObj.playGame(dataSet)
    simpleCollisionsL.append(sCollisons)
    
    optimizeCollisionsL.append(oCollisions)
    dataSet = optimizeGameObj.getData()

    if len(optimizeCollisionsL) == 100:
        return (simpleCollisionsL, optimizeCollisionsL)
    else:
        # Resets games without changing random probablilties 
        simpleGameObj.reset()
        optimizeGameObj.reset()
        # Recursive call
        return optimizeGame(simpleGameObj, optimizeGameObj, dataSet, simpleCollisionsL, optimizeCollisionsL)

def main():
    """
    Runs the optimization given game parameters and plots results.

    :param: None.
    :return: None.
    """
    M = None
    S = None

    try:
        M = int(input("Input the number of tracks: "))
        S = int(input("Input the time that the player stays on each track before jumping to another: "))
        while M <= 1 or S <=0:
            M = int(input("Incorrect. Input the number of tracks: "))
            S = int(input("Incorrect. Input the time that the player stays on each track before jumping to another: "))
    except:
        print("Your input was invalid!")
        main()
    sGame = SimpleAlgorithmGame(M,S)
    oGame = Optimize(M, S, [ [] ]*M)
    blockPrint()
    dataPoints = optimizeGame(sGame, oGame, [ [] ]*M)
    enablePrint()
    plt.plot(dataPoints[0], label="Simple Algorithm")
    plt.plot(dataPoints[1], label="Opptimized Algorithm")
    plt.ylabel('Number of Collisions')
    plt.xlabel('Number of games played')
    plt.xlim(xmin=1)
    #plt.ylim(0,100)
    #plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()