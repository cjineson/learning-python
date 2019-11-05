# Rock Paper Scissors
import random
str_list = ['Rock','Paper','Scissors']

your_int = int(input("Enter number 1:Rock/2:Paper/3:Scissors:"))-1
your_str = str_list[your_int]

my_int = random.randint(0,2)
my_str = str_list[my_int]

print("You: ",your_str)
print("Me:  ",my_str)

if (my_int == 0) & (your_int == 2):
    print("I win!")
elif my_int == your_int:
    print("Draw!")
elif (your_int == 0) & (my_int == 2):
    print("You win!")
elif my_int > your_int:
    print("I win!")
else:
    print("You win!")