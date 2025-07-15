#Q1 - print 1 to 100
count = 0
while count <= 100:
    print(count)
    count+=1
    
#Q2 - print 100 to 1
count = 100
while count >= 1:
    print(count)
    count-=1
    
#Q3 - multiplication of number n
n = int(input("enter a number for multiplication: "))
count = 0
while count <= 12:
    print(n*count)
    count +=1
    
#Q4 - print the elements of the list
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index < len(list):
    print(list[index])
    index+=1
    
#Q5 - search a number from a tuple using loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
a = 36
index = 0
while index < len(tup):
    if(tup[index] == a):
        print("element found at index: ", index)
    else:
        print("element not found.")
    index+=1
    
#Q6 - print elements using for loop
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for a in list:
    print(a)
    
#Q7 - search a number using for loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
s = int(input("enter the number to search: "))
index = 0
for b in tup:
    if(b == s):
        print("element found at index: ", index)
        break;
    index+=1
else:
        print("element not found")
        
#Q8 - print 1 to 100 using for loop & range
for i in range(101):
    print(i)
    
#Q9 - print 100 to 1 using for loop & range
for i in range (100, 0, -1):
    print(i)
    
#Q10 - print the multiplication table of number n using for loop & range
n = int(input("enter a number: "))
for i in range(1, 13):
    print(n*i)
    
#Q11 - find the sum of first n numbers using the while loop
n = int(input("enter a number: "))
i = 0
sum = 0
while i<=n:
    sum += i
    i+=1
print(sum)

#Q12 - find the factorial of first n numbers using for loop
n = int(input("enter a number: "))
fac = 1
for i in range(1, n+1):
    fac *= i
print(fac)