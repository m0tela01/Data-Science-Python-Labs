import time
import numpy as np
import math
from itertools import combinations

## need to press enter to start the window for pygame
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("{ENTER}")
import pygame
pygame.init()


### Exercise 7.10 problem break down
    ## play two-dimensional Tic-Tac-Toe between two people enterint their moves
    ## game is played on the same computer
    ## 3x3 array for the board
    ## player should indicate move by entering two numbers for row and column indices
    ## player 1 is X, player 2 is O
    ## moves must be for empty squares
    ## determine if game is over after each round whether its a draw or win

class tickTackToe():
    '''Class for the Tick-Tack-Toe game.'''

    # the board definitions for the coordinates and positions
    board = {
        "TOP_LEFT": [1, pygame.Rect(1,1, 199,199), (80,80)],
        "TOP_MID": [2, pygame.Rect(201,1, 401,199), (280,80)],
        "TOP_RIGHT": [3, pygame.Rect(402,1, 603,199), (480,80)],
        
        "MID_LEFT": [4, pygame.Rect(1,199, 199,399), (80,280)],
        "CENTER": [5, pygame.Rect(201,201, 399,399), (280,280)],
        "MID_RIGHT": [6, pygame.Rect(402,201, 603,399), (480,280)],

        "BOT_LEFT": [7, pygame.Rect(1,402, 199,603), (80, 480)],
        "BOT_MID": [8, pygame.Rect(201,402, 399,603), (280,480)],
        "BOT_RIGHT": [9, pygame.Rect(402,402, 603,603), (480,480)],
    }

    # the win senarios
    win = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]
    ]

    def __init__(self, start=True, tickTackToeBoard=board, winMoves=win):
        '''Initialize Tick Tack Toe.'''
        self.simulate = start
        self.width = 604
        self.height = 604
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Comic Sans MS', 40) 
        self.board = tickTackToeBoard
        self.win = np.array(winMoves)
        self.winMessage = ""

        self.xTurn = True
        self.xText = self.font.render("X", True, (0,0,0))
        self.oText = self.font.render("O", True, (0,0,0))
        
        ## use these later
        # self.x = 0
        # self.y = 0

        self.player1 = []
        self.player2 = []

        
    def resetGame(self, event):
        '''Resets the game if the game is over. Redraws the board and resets the players positions.'''
        if event.type == pygame.QUIT:
            pygame.quit()
        else:
            self.simulate = True
            self.xTurn = True
            self.player1 = []
            self.player2 = []
            self.screen.fill((33,206,153))
    
        pygame.draw.line(self.screen, (0,0,0), (int((self.width-2)/3), 1), (int((self.width-2)/3), 603), 1)
        pygame.draw.line(self.screen, (0,0,0), (int(2 * (self.width-2)/3), 1), (int(2 * (self.width-2)/3), 603), 1)

        pygame.draw.line(self.screen, (0,0,0), (1, int((self.width-2)/3)), (603, (int(self.width-2)/3)), 1)
        pygame.draw.line(self.screen, (0,0,0), (1, int(2 * (self.width-2)/3)), (603, int(2 * (self.width-2)/3)), 1)
        pygame.display.flip()        

    def checkPlayerMove(self, moves, player):
        '''Test if the player has won by checking all the combinations of their moves.'''
        moves = list(combinations(moves, 3))
        for move in moves:
            if (self.win == move).all(1).any():
                self.simulate = False
                self.winMessage = self.font.render(player, True, (0,0,0))
                self.screen.blit(self.winMessage, (220, 20))
                self.screen.blit(self.winMessage, (220, 220))
                self.screen.blit(self.winMessage, (220, 420))
                pygame.display.flip()
                time.sleep(2.0)
                break

    def checkGame(self):
        '''Let each senario by tested if someone wins display they won. If its a draw
        show it is a draw. 
        '''
        if len(self.player1) >= 3:
            moves = np.array(self.player1)
            moves.sort()
            self.checkPlayerMove(moves, "X's win!")
        if len(self.player2) >= 3:
            moves = np.array(self.player2)
            moves.sort()
            self.checkPlayerMove(moves, "O's win!")
        if len(self.player1) + len(self.player2) is 9 and self.simulate is True:
            self.simulate = False
            self.winMessage = self.font.render("  Draw", True, (0,0,0))
            self.screen.blit(self.winMessage, (220, 220))
            pygame.display.flip()
            time.sleep(2.0)

    def doMove(self, drawLocation, boardLocation):
        '''Performs the move for a player if the square is clicked then check that no one has been there
        already. If it is repeated the player keeps their turn but nothing happens. If the move works out
        add that to the players list of moves.
        '''
        if len(self.player1) is 0:
            print('X')
            self.screen.blit(self.xText, drawLocation)
            self.player1.append(self.board[boardLocation][0])
            self.xTurn ^=True
        else:
            if len(self.player2) is 0 and self.board[boardLocation][0] not in self.player1:
                print('O')
                self.screen.blit(self.oText, drawLocation)
                self.player2.append(self.board[boardLocation][0])
                self.xTurn ^=True
            else:
                if self.board[boardLocation][0] in self.player1 or self.board[boardLocation][0] in self.player2:
                    print("cannot be in same box")
                else:
                    if self.xTurn:
                        print('X')
                        self.screen.blit(self.xText, drawLocation)
                        self.player1.append(self.board[boardLocation][0])
                    else:
                        print('O')
                        self.screen.blit(self.oText, drawLocation)
                        self.player2.append(self.board[boardLocation][0])

                    self.xTurn ^=True
    
    def drawer(self):
        '''Draws the game by calling resetGame initially. Events are driven by mouse position in this game.
        If a player clicks inside a box a character will be drawn in the middle. Each coordinate is mapped
        to the self.board which is accessed when a point 'collides' with the coordinate in the board.
        The order of the coordinates is weird but it would not work in the logical order (they are shuffled).
        '''
        self.resetGame(pygame.event.get()[0])

        while self.simulate is True:
            for event in pygame.event.get():
                # self.x, self.y = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.simulate = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button.
                        if self.board["TOP_LEFT"][1].collidepoint(event.pos):
                            self.doMove(self.board["TOP_LEFT"][2], "TOP_LEFT")
                        elif self.board["BOT_LEFT"][1].collidepoint(event.pos):
                            self.doMove(self.board["BOT_LEFT"][2], "BOT_LEFT")
                        elif self.board["BOT_RIGHT"][1].collidepoint(event.pos):
                            self.doMove(self.board["BOT_RIGHT"][2], "BOT_RIGHT")
                        elif self.board["BOT_MID"][1].collidepoint(event.pos):
                            self.doMove(self.board["BOT_MID"][2], "BOT_MID")
                        elif self.board["TOP_RIGHT"][1].collidepoint(event.pos):
                            self.doMove(self.board["TOP_RIGHT"][2], "TOP_RIGHT")
                        elif self.board["TOP_MID"][1].collidepoint(event.pos):
                            self.doMove(self.board["TOP_MID"][2], "TOP_MID")
                        elif self.board["MID_LEFT"][1].collidepoint(event.pos):
                            self.doMove(self.board["MID_LEFT"][2], "MID_LEFT")
                        elif self.board["MID_RIGHT"][1].collidepoint(event.pos):
                            self.doMove(self.board["MID_RIGHT"][2], "MID_RIGHT")
                        elif self.board["CENTER"][1].collidepoint(event.pos):
                            self.doMove(self.board["CENTER"][2], "CENTER")
                        else:
                            print("o h  n o  n o  n o  n o  n o")
                    pygame.display.flip()
                
                self.checkGame()

                if self.simulate is False:
                    self.resetGame(event)
        

def main():   
    
    t = tickTackToe()
    t.drawer()

if __name__ =="__main__": main()
