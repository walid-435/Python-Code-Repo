name=input("Enter your first name: ")
print(len(name))

dolla="i've very very $ in my pocket, i love $. $ is life"
print(dolla.count("$"))

# #practice conditional sentences

marks=int(input("Enter the marks: "))

if(marks>=90):
    print("Your grade is A.")
elif(90>marks>=80):
    print("Your grade is B")
elif(80>marks>=70):
    print("Your grade is C")
elif(60<=marks<70):
    print("Your grade is D")
else:
    print("Your grade is F")
    
#pcs1

number=int(input("Enter a numebr: "))

if(number%2==0):
    print("The numeber is even")
else:
    print("The numeber is odd")
    
#pcs2

num1=int(input("First number: "))
num2=int(input("Second number: "))
num3=int(input("Third number: "))

if(num1>num2 and num1>num3):
    print("Number one greates")
elif(num2>num1 and num2>num3):
    print("Number two greates")
else:
    print("Number three greates")
    
#pcs3

mul=int(input("Enter a number: "))

if(mul%7==0):
    print("Multiple of 7")
else:
    print("Is not the multiple of 7")