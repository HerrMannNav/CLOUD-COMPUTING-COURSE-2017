import random
import re

def representsInteger(i):
    return re.match(r"[-+]?\d+$", i)
    
minNumber, maxNumber = 0, 20

randomNumber = random.randint(minNumber, maxNumber)
print randomNumber

inputNumber = raw_input("Guess the number! [" + str(minNumber) + "," + str(maxNumber) + "]\t")

while True:
    if representsInteger(inputNumber):
        inputNumber = int(inputNumber)
        if inputNumber > randomNumber: 
            inputNumber = raw_input("Try a lesser one!\t")
        elif inputNumber < randomNumber:
            inputNumber = raw_input("Try a greater one!\t")
        else:
            print "GREAT!"
            exit(0)
    else: inputNumber = raw_input("Write an INTEGER NUMBER!\t")