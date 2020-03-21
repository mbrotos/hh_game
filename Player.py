import random
class Player:
    """
    Player encapsulates a hogwartz game and helping functions.
    """
    
    def __init__(self, health=100, current_track=0):
        """
        Construct a new 'Main' object.

        :param health: The starting health of the player
        :param current_track: The track that the player is currently on.
        :return: returns nothing
        """
        self.health = health
        self.current_track = current_track
        self.tOnCurTrack = 0

    def get_health(self):
        return self.health

    def get_current_track(self):
        return self.current_track

    def set_current_track(self, track):
        self.current_track = track

    def set_health(self, new_health):
        self.health = new_health

    def getTOnCurTrack(self):
        return self.tOnCurTrack

    def setTOnCurTrack(self, time):
        self.tOnCurTrack = time

    def __str__(self):
        return "Player is on track: {} and has {} health. ".format(self.current_track, self.health)

class Hobo(Player):
    """
    Main encapsulates a hogwartz game and helping functions.
    """
    #State variables
    messagesList = [
        "Oi bruv, track {} appears a bit dodgy.",
        "A charmin’ little bloke aren’t ye’? Don’t fall arse over tit dodgin’ the train approachin’ track {}.",
        "Mate, Pissed Peter is off his rockers! He started spewin’ crap about how a train would be comin’ through track {} which is completely bonkers! Poor bloke been gettin’ pissed drunk ever since his wife an’ child left ‘im…",
        "You remind me of this one chap I met a while back. Name was Harry I believe. Thought ‘imself to be a damn wizard! Anyhow, a train is headin’ your way on track {}.",
        "A complete nutjob you are mate! You must be sloshed my friend but I’m feeling kind meself. Steer clear of track {} if you wan’a live!",
        "Bruv, me and me mom ‘ave been livin’ on these tracks far before you were born! Don’t be a complete tit and be cautious of the train on track {} if you don’t want to make a complete fool out of yourself!" ,
        "Me mate and I met Dumbledore but he went off sayin’ that it was some bloke named 'Gandalf' instead! Could you believe the porkies ‘e was spoutin’?? Unlike me mate, I ‘ont lie to you! Avoid track {} at all costs!",
        "Life has never been kind to me, mon ami. I have been on ze run from  l’officiels de français for my whole life. Vas-y mon jeune ami! Le train is approaching on ze track {}!",
        "You-! I saw ye’ in me dream! May the great wizards of Hogwarts guide you! It feels like fate has brought us together, innit bruv? They are telling me to tell you to stay clear of track {}, your nemesis, a train, is approaching!" ,
        "Knight of Computer Science! Tread carefully as you advance forward through the tunnel of despair! A little tip to you, fledgling knight! Track {} is riddled with beasts that you must stay away from! May the Gods ever be on your side!"
    ] 

    
    def __init__(self, health, current_track, M):
        """
        Construct for a hobo, whether player or non-player(default non-player).

        :param health: The starting health of the player
        :param current_track: The track that the player is currently on.
        :return: returns nothing
        """
        super(health, current_track)
        self.numOfTracks = M



    def airPlaneMsg(self):
        """
        Selects a random message from the Hobo.

        :return: a string containing a message from the hobo
        """
        airplane_prob = random.randint(1, 10)

        if airplane_prob == 1:
            return (random.choice(self.messagesList)).format(random.randint(1,self.numOfTracks))

        elif airplane_prob == 2:
            return "You missed an Airplane!"

        else:
            return None
