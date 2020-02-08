import random
import time
import numpy as np
import math
import pandas as pd
import sys

import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("{ENTER}")
import pygame
pygame.init()

VK_RETURN = 0x0D                # ENTER key

### Exercise 6.8 problem break down
    ## create a dictionary that maps numbers to their corresponding word equivalents
    ## takes as an input a number less than 1000 and outputs the words of that amount
    ## if input 112.43 output is ONE HUNDRED TWELVE AND 43/100


class helper:
    '''Class for misc functions.'''
        
    dictOfNumbers = {
        -1: "AND",
        0: "ZERO",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE",
        10: "TEN",
        11: "ELEVEN",
        12: "TWELVE",
        13: "THIRTEEN",
        14: "FOURTEEN",
        15: "FIFTHTEEN",
        16: "SIXTEEN",
        17: "SEVENTEEN",
        18: "EIGHTEEN",
        18: "NINETEEN",
        20: "TWENTY",
        30: "THIRTY",
        40: "FOURTY",
        50: "FIFTY",
        60: "SIXTY",
        70: "SEVENTY",
        80: "EIGHTY",
        90: "NINETY",
        100: "HUNDRED"
    }

    def __init__(self, words=dictOfNumbers):
        self.words = words
        self.elements = []
        self.places = []
    
    def dictJoiner(self, element):
        self.elements.append(self.words[element])

    def dictResolver(self, value=str(input())):
        numbers = [-1 if number is "." else int(number) for number in value]
        cents, index = 0, 0
        if len(numbers) > 1:
            if (-1 in numbers) is True:
                numbers = np.array(numbers)
                decimals = numbers[np.where(numbers == -1)[0][0] +1:]
                cents = ''.join(map(str, decimals)) + "/100"

                numbers = numbers[:np.where(numbers == -1)[0][0]]
                
                try:
                    if len(numbers) is not 0:
                        for number in numbers[::-1]:
                            number *= math.pow(10, index)
                            if index is 2:
                                number /= 100
                                self.elements = [self.words[100]] + self.elements

                            self.elements = [self.words[int(number)]] + self.elements
                            index += 1
                        self.elements.append(self.words[-1])
                except:
                    pass

                self.elements.append(cents)
                
        else:
            print(self.words[numbers[0]])


    def print(self, args):
        print(*args)


class tickTackToe():
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
    win = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,6],
        [3,6,9],
        [1,5,9],
        [3,5,7]

    ]

    def __init__(self, start=True, tickTackToeBoard=board, winMoves=win):
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
        self.x = 0
        self.y = 0

        self.player1 = []
        self.player2 = []

        
    def doMove(self, drawLocation, boardLocation):
        if self.xTurn:
            print('X')
            self.screen.blit(self.xText, drawLocation)
            self.player1.append(self.board[boardLocation][0])
        else:
            print('O')
            self.screen.blit(self.oText, drawLocation)
            self.player2.append(self.board[boardLocation][0])

        self.xTurn ^=True


    def checkGame(self):
        
        if len(self.player1) is 3:
            moves = np.array(self.player1)
            moves.sort()
            if (self.win == moves).all(1).any():
                self.simulate = False
                self.winMessage = self.font.render("X's win!", True, (0,0,0))
                 self.screen.blit(self.winMessage)

        if len(self.player2) is 3:
            moves = np.array(self.player2)
            moves.sort()
            if (self.win == moves).all(1).any():
                self.simulate = False
                self.winMessage = self.font.render("O's win!", True, (0,0,0))
                self.screen.blit(self.winMessage)


    
    def drawer(self):
        self.screen.fill((33,206,153))
    
        pygame.draw.line(self.screen, (0,0,0), (int((self.width-2)/3), 1), (int((self.width-2)/3), 603), 1)
        pygame.draw.line(self.screen, (0,0,0), (int(2 * (self.width-2)/3), 1), (int(2 * (self.width-2)/3), 603), 1)

        pygame.draw.line(self.screen, (0,0,0), (1, int((self.width-2)/3)), (603, (int(self.width-2)/3)), 1)
        pygame.draw.line(self.screen, (0,0,0), (1, int(2 * (self.width-2)/3)), (603, int(2 * (self.width-2)/3)), 1)
        pygame.display.flip()

        while self.simulate is True:
            for event in pygame.event.get():
                self.x, self.y = pygame.mouse.get_pos()

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
        

        


def main():
    # h = helper()
    # h.dictResolver()
    # h.print(h.elements)

    

    
    
    
    t = tickTackToe()
    t.drawer()



if __name__ =="__main__": main()



