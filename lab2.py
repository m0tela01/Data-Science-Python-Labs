

class Lab2:
    
    def ex3_ReverseString():
        letters = list(input())
        output = []
        def reverse(output, letters):
            if len(letters) > 0:
                output.append(letters.pop(len(letters) - 1))
                reverse(output, letters)
            
        reverse(output, letters)
        print("".join(output))

    def ex4_Sort():
        output = ""
        searchString = input()
        pattern = input()
        import re
        for letter in pattern:
            if letter in searchString:
                output += str(letter * len(re.findall(letter, searchString)))
        print(output)


    def ex7_Factorial():
        output = 1
        
        def factor(fact, output):
            if fact > 0:
                output *= fact
                fact -= 1
                factor(fact, output)
            else:
                print(output)
        
        factor(int(input()), output)
    
    def ex8_1toN():
        lastElement = int(input())
        output = [1]
        def increment(output, lastElement):
            if len(output) is not lastElement:
                output.append(max(output) + 1)
                increment(output, lastElement)

        increment(output, lastElement)
        print(*output)
    
    def ex10_Mul2Ints():
        output = 0

        def mul(num1, num2, output):
            if num2 > 0:
                output += num1
                num2 = num2 - 1
                mul(num1, num2, output)
            else:
                print(output)

        mul(int(input()), int(input()), output)

Lab2.ex4_Sort()