# Password generator
import sys, getopt, random, string
print("Generating Password")
length = 0 

if len(sys.argv) > 1:
    length = int(sys.argv[1])
    print('Password length:',length)
else:
    length = int(input("Password length:"))
    print('Password length:',length)

i = 1
while i<length:
    sys.stdout.write(random.choice(string.ascii_letters))
    sys.stdout.flush()
    i=i+1
print