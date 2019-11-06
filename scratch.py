# String variables, assignment, expressions, If statement
mystring = "A String"
yourstring = 'Another String'
print(mystring)
print(yourstring)
print(mystring == yourstring)
if mystring != yourstring:
    mystring = mystring.replace("A ","Another ")
    print(mystring)
print(mystring == yourstring)

# Integer variables, While loop, arithmetic expression
myint = 1
yourint = 10
print(myint)
print(yourint)
print(myint == yourint)
print(myint < yourint)
while myint < yourint:
    print(myint)
    myint = myint + 1
print(myint == yourint)

# List, array indices, For loop
mylist = ["Tinker","Tailor","Soldier","Sailor"]
print(mylist)
print(mylist[3])
for item in mylist:
    print(item)

