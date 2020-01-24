import random
import time


### problem break down
    ## use randomness
    ## start at square 1 win at or grater than square 70
    ## winner gets a pile of carrots and lettuce
    ## occasionally lose ground because of mountain path
    ## clock time is one iteration of moveing/turn -- one turn per second
    ## use variables to keep track of the positions of the animals (1-70)

    ## if slipping left before square 1 move to square 1

    ## produce a table wih precentages for a random variable "i" in range [1,10]
    ## if the tortoise rolls between [1,5] it is fast, [6,7] it is a slip, [8, 10] it is slow
    ## same for the hare

    ## start the race by printing "BANG!!!!!AND THEY'RE OFF!!!!!"
    ## every iteration should show a line of length 70 which represents the race positions
    ## these should show a "T" and "H" for the tortoise and Hare respectively
    ## if both land in the same square tortoise bites hare and print "OUCH!!!"
    ## after displaying the move/turn check if H/T position is >= 70
    ## if true for T print "TORTOISE WINS!!! YAY!!!"
    ## if true for H print "Hare wins. Yuch"
    ## if there is a tie either favor T as "underdog" or print "it's a tie"


class Helper:
    '''Class for misc functions.
    '''
    ## constants
    STARTMESSAGE = "BANG!!!!!AND THEY'RE OFF!!!!!"

    def __init__(self, start=STARTMESSAGE):
        '''Initialize Helper.
        '''        
        self.clock = 0
        self.startMessage = start

    def getClock(self):
        '''Getter.
        '''      
        return self.clock

    def setClock(self, i=1):
        '''Setter. Also increments the clock.
        '''        
        self.clock += i


    def printStart(self):
        '''Print the start message.
        '''
        print(self.startMessage)


    def roll(self):
        '''Performs a roll in range [1,10]. Used to retrieve the "table" value.
        '''
        return random.randrange(1, 11)
    
    def print(self, args):
        '''A printer. It sleeps for a bit so you can watch.
        '''
        print('{:<4}{:<}{:<}{:<}'.format(*args))
        time.sleep(0.07)



class Player:
    '''Class for a race participant in the historical race.
    '''
    ## constants
    ## 69 displayed squares because each player takes 1 space
    RACELINE = "______________________________________________________________________"   

    TIE_MESSAGE = "it's a tie"
    COLLISION_MESSAGE = "OUCH!!!"

    TORTOISE_WIN_MESSAGE = "Ⓣ ORTOISE WINS!!! YAY!!!"
    HARE_WIN_MESSAGE = "Ⓗ are wins. Yuch"
    T, H = "Ⓣ", "Ⓗ"

    T_MOVES = {1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: -6, 7: -6, 8: 1, 9: 1, 10: 1}
    H_MOVES = {1: 0, 2: 0, 3: 9, 4: 9, 5: -12, 6: 1, 7: 1, 8: 1, 9: -2, 10: -2}

    def __init__(self, setOfPossibleMoves, wMessage):
        '''Initialize Player.
        '''
        self.location = 1
        self.hasWonRace = False
        self.moves = setOfPossibleMoves
        self.winMessage = wMessage

    def getLocation(self):
        '''Getter.
        '''              
        return self.location
    
    def setLocation(self, roll):
        '''Setter. Get move based on roll as an index of the players moves dictionary. 
        Resets position to 1 if location < 1 or to 70 if location > 70.
        '''      
        self.location += self.moves[roll]
        if (self.location < 1):
            self.location = 1
        if (self.getLocation() > 70):
            self.location = 70


    def moveString(self, t_location, h_location):
        '''Create race line string based on moves. If they dont collide insert players location into string.
        If collision print message.
        '''
        raceLine = Player.RACELINE
        if t_location != h_location:
            raceLine = raceLine[:t_location] + self.T + raceLine[t_location:]
            raceLine = raceLine[:h_location] + self.H + raceLine[h_location:]
            return raceLine
        else:
            raceLine = raceLine.replace(raceLine[0], "", 5)
            raceLine = raceLine[:len(raceLine)//2] + self.COLLISION_MESSAGE + raceLine[len(raceLine)//2:]
            return raceLine

    def isRaceOver(self):
        '''Check if player is at finish line. If they set won race true.
        '''
        if self.getLocation() == 70:
            self.hasWonRace = True



def main():
    ## initialize players & judge
    judge = Player({}, "")
    tortoise = Player(Player.T_MOVES, Player.TORTOISE_WIN_MESSAGE)
    hare = Player(Player.H_MOVES, Player.HARE_WIN_MESSAGE)

    ## initialize helper & print starting message
    helper = Helper()
    helper.printStart()

    ## run until either player has won the race 
    while not (tortoise.hasWonRace | hare.hasWonRace):
        helper.setClock()   ## update clock value

        ## roll the value for the current round of the players
        tortoise.setLocation(helper.roll())
        hare.setLocation(helper.roll())

        ## check and set status of player 
        tortoise.isRaceOver()
        hare.isRaceOver()
        
        ## build and then print current iteration
        helper.print([helper.getClock(), "  ▓  ", judge.moveString(tortoise.getLocation(), hare.getLocation()), "  ░  "])

    ## displays the outcome of the race
    if tortoise.hasWonRace and hare.hasWonRace:
        print(judge.TIE_MESSAGE)
    elif tortoise.hasWonRace:
        print(judge.TORTOISE_WIN_MESSAGE)
    else:
        print(judge.HARE_WIN_MESSAGE)
        




if __name__ =="__main__": main()