# import os
# import numpy as np
# import re
# import sys
# import pandas as pd
# from matplotlib import pyplot as plt
# import seaborn as sns

class LAB1:
    def ex1_MagicNumber():
        """ Exercise 11.1
        Magic number.
        Given an integer N, find whether the numbers is a magic number or not. 
        """
        N = int(input())
        N = [int(digit) for digit in str(N)]

        while len(N) > 1:
            N = sum(N)
            N = [int(digit) for digit in str(N)]

        if sum(N) != 1:
            print('0')
        else:
            print(str(sum(N)))


    def ex2_ReadFloat():
        """ Exercise 11.2
        Read float value from input and display it.
        """
        N = float(input())
        print(format(N, '.2f'))


    def ex3_DisariumNumber():
        """ Exercise 11.3
        Disarium Number.
        Given an integer N, find whether N is a Disarium or not. 
        """       
        N = int(input())
        iN = N
        N = [int(digit) for digit in str(N)]
        res = 0

        for index, number in enumerate(N):
            res += number**(index + 1)
        if res == iN:
            print('1')
        else:
            print('0')


    def ex4_SumOneToN():
        """ Exercise 11.4
        Sum of 1 to N numbers
        """
        N = int(input())
        sumM = 0
        for number in range(0, N+1):
            sumM += number;
            number += 1
        print(sumM)


    def ex5_DiamondPattern():
        """ Exercise 11.5.
        Number Pattern - Diamond number pattern.
        1
        1 2 3
        1 2 3 4 5
        1 2 3 4 5 6 7
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7
        1 2 3 4 5
        1 2 3
        1
        """
        N = int(input())
        counter = N
        print(1)
        for row in range(1, 2*N - 1):
            res = [1]
            if row < N:
                for column in range(0, 2*row):
                    res.append(column + 2)
            else:
                counter -=1
                for column in range(2, 2*counter):
                    res.append(column)
                    
            res = list(map(str, res))
            print(' '.join(res))


    def ex6_ReadChar():
        """ Exercise 11.6.
        Read Character from keyboard and display on console.
        """
        N = input()
        print(N)


    def ex7_PerfectNumber():
        """ Exercise 11.7.
        Find the perfect numbers within a given range.
        A Perfect number is a positive number, for which sum of all positive divisors of that number excluding that number is equal to that number.
        e.g. 6 is a perfect number since divisor of 6 are 1, 2 and 3. Sum of its divisor is 1 + 2 + 3 = 6.
        """
        N1 = int(input())
        N2 = int(input())

        def perfectNumber(N1, N2):
            result = []
            while N1 < N2:
                i = 1
                divisors = []
                while i < N1:
                    if N1 % i == 0:
                        divisors.append(i)
                    i += 1
                if sum(divisors) == N1:
                    result.append(N1)
                N1 += 1
            return result

        print(*perfectNumber(N1, N2))
    

    def ex8_SumOfSeries():
        """ Exercise 11.8.
        Find the sum of the series 1-(X^2)/2!+(X^4)/4!-...
        """
        import math
        X = int(input())
        N = int(input())
        power, result = 2, 1
        subFirst = False

        for idx in range(1, N):
            if subFirst == True:
                result += math.pow(X, power)/math.factorial(power)
                subFirst = False
            else:
                result -= math.pow(X, power)/math.factorial(power)
                subFirst = True
            power += 2
        print(format(result, '.3f'))


    def ex9_SumOfSeries():
        """Exercise 11.9.
        Find the sum of the series X - X^3 + X^5 -...
        """
        import math
        X = int(input())
        N = int(input())
        power, result = 3, X
        subFirst = False
        for idx in range(1, N):
            if subFirst is True:
                result += math.pow(X, power)
                subFirst = False
            else:
                result -= math.pow(X, power)
                subFirst = True
            power += 2
        print(str(int(result)))


    def ex10_StarPattern():
        """ Exercise 11.10.
        Star pattern - Hollow Pyramid star pattern.
                *
              *   *
            *       *
          *           *
        * * * * * * * * *
        """
        N = int(input())
        rightSpaceSize = 3
        leftSpaceSize = N * 2 - 2
        space, star = ' ', '*'

        for idx in range(1, N + 1):
            if idx is 1:
                print((space * leftSpaceSize) + star)
                leftSpaceSize -= 2
            elif idx is not N:
                print((space * leftSpaceSize) + star + (space * rightSpaceSize) + star)
                rightSpaceSize += 4
                leftSpaceSize -= 2
            else:
                lastRow = star
                for idx in range(0, (N * 2 - 2)):
                    lastRow += (space + star)
                print(lastRow)

