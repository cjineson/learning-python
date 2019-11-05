import sys, random

# Generate random number & prompt user to guess until correct
NUM_FROM = 1
NUM_TO = 10

randnum = random.randrange(NUM_FROM,NUM_TO)
    
while True:
    
    # print(sys.version_info)
    
    if sys.version_info.major < 3:
        response = raw_input('Guess the number:')        
    else:
        response = input('Guess the number:')
    
    if int(response) == randnum:
        print("Yay")
        break

