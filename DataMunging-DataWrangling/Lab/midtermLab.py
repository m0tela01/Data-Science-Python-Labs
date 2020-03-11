# import os
# import numpy as np
# import re
# import sys
# import pandas as pd
# from matplotlib import pyplot as plt
# import seaborn as sns

import itertools

class Midterm:
    def __init__(self):
        self.output = []
        self.increment = 1
        self.elements = []
        self.numOfElements = 0
        self.plainText = []
        self.keyword = []


    def getElements(self):
        self.numOfElements = int(input())
        self.elements = [int(ele) for ele in str.split(input(), " ")]
    
    def getStrings(self):
        self.plainText =  list(input().upper())
        self.keyword = list(input().upper())
        
    def ex1_Sums(self):        
        if self.numOfElements is not None and self.numOfElements is not 0 and self.increment <= self.numOfElements:
            size = self.increment
            
            for i in range(0, int(self.numOfElements)):
                if size is 1:
                    self.output.append(self.elements[i])
                else:
                    self.output.extend([sum(sett) for sett in itertools.combinations(self.elements, size)])

            self.increment += 1
            self.ex1_Sums()
        else:
            print(*set(self.output))
            self.elements = []
            self.increment = 1
            self.output = []
    
        
    def ex2_mins(self):
        minimum = min(self.elements)
        index1, index2 = 1001, 0
        indiciesA = []
        for i in range(0, len(self.elements)):
            if minimum is self.elements[i]:
                sameIdx = True
                indiciesA.append(i)
        for i in range(0, len(indiciesA) - 1):
            best = abs(index1 - index2)
            test = abs(indiciesA[i] - indiciesA[i+1])
            if test < best:
                self.output[0] = test

        print(self.output[0])

    def ex3_cipher(self):
        uniqueLetters = []
        alphabet1 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        alphabet1 = str.split(alphabet1, " ")
        newAlphabet = alphabet1.copy()
        [newAlphabet.remove(ele) for ele in self.keyword if ele in newAlphabet]
        [uniqueLetters.append(ele) for ele in self.keyword if ele not in uniqueLetters]
        newAlphabet = uniqueLetters + newAlphabet
        
        for letter in self.plainText:
            if letter is ' ':
                self.output.append(' ')
            else:
                originalIndex = alphabet1.index(letter)
                self.output.append(newAlphabet[originalIndex])

        print("".join(self.output))



        

def main():
    midterm = Midterm()
    # midterm.output.append(0)
    # midterm.getElements()
    # midterm.ex1_Sums()
    
    # midterm.output.append(0)
    # midterm.getElements()
    # midterm.ex2_mins()

    midterm.getStrings()
    midterm.ex3_cipher()


if __name__ =="__main__": main()