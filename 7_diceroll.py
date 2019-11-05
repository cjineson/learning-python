import sys, random

# Enforce Python3
if sys.version_info[0] < 3:
    raise Exception("Python 3 only")

# Roll dice while user input y
NUM_FROM = 1
NUM_TO = 6

keeprolling = True
while keeprolling:
    print(random.randrange(NUM_FROM,NUM_TO))

    response = input('Keep rolling? (y/n)')
    
    if response == 'y':
        keeprolling = True
    else:
        keeprolling = False
