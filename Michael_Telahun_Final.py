import re

class Final:
    
    start = 0
    
    def cleanString(self, string):
        reg = "[^A-z]"
        regexp = re.compile(reg)
        return regexp.sub('', string)


    def paladin(self, string, i=start):
        if len(string) is 1:
            return True

        if string[i] is not string[len(string) - i - 1]:
            return False
        
        if i < len(string) - i:
            i += 1
            return self.paladin(string, i)
        
        return True


final = Final()
print(final.paladin(final.cleanString("a12 a")))





