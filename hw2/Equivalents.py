import numpy as np

### Exercise 6.8 problem break down
    ## create a dictionary that maps numbers to their corresponding word equivalents
    ## takes as an input a number less than 1000 and outputs the words of that amount
    ## if input 112.43 output is ONE HUNDRED TWELVE AND 43/100

class equivalents:
    '''Class for equivalents of number to string.
    '''
    
    # dictionary of numbers to strings used 
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
        19: "NINETEEN",
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
        '''Initialize equivalents.'''
        self.words = words
        self.elements = []
        self.places = []
    

    def dictResolver(self, value=str(input("Enter a number less than 4 digits: "))):
        '''Takes a number as an input and converts it to the string equivalent format in the 
        the problem description. This only works for 3 digit numbers. Probably overcomplicated.
        '''
        numbers = [-1 if number is "." else int(number) for number in value]
        cents, index = 0, 0
        if len(numbers) > 1:
            if (-1 in numbers) is True:
                numbers = np.array(numbers)
                decimals = numbers[np.where(numbers == -1)[0][0] +1:]
                cents = ''.join(map(str, decimals)) + "/100"

                numbers = numbers[:np.where(numbers == -1)[0][0]]
                numbers = np.array(numbers)
                numbers = numbers[::-1]
                tens = ''.join(map(str,numbers[1:]))
                if len(numbers) is 1:
                    self.elements = [self.words[numbers[0]]]
                else:
                    if int(tens) < 20:
                        self.elements = [self.words[int(tens)]]
                    else:
                        self.elements = [self.words[int(numbers[0])]] + self.elements
                        self.elements = [self.words[int(numbers[1] * 10)]] + self.elements
                    if len(numbers) > 2:
                        hundreds = numbers[2]
                        self.elements = [self.words[100]] + self.elements

                        self.elements = [self.words[int(hundreds)]] + self.elements
                        index += 1                      
                
                self.elements.append(self.words[-1])
                self.elements.append(cents)
            else:
                numbers = np.array(numbers)
                numbers = numbers[::-1]
                tens = ''.join(map(str,numbers[1:]))
                if int(tens) < 20:
                    self.elements = [self.words[int(tens)]]
                else:
                    self.elements = [self.words[int(numbers[0])]] + self.elements
                    self.elements = [self.words[int(numbers[1] * 10)]] + self.elements
                if len(numbers) > 2:
                    hundreds = numbers[2]
                    self.elements = [self.words[100]] + self.elements

                    self.elements = [self.words[int(hundreds)]] + self.elements
                    index += 1          

            self.print(self.elements)
        else:                
            if len(numbers) is 1:
                print(self.words[numbers[0]])

    def print(self, args):
        '''Prints arrays.'''
        print(*args)


def main():
    h = equivalents()
    h.dictResolver()


if __name__ =="__main__": main()
