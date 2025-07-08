#logical operator

a=50
b=30
print(not False)
print(not (a>b))

value1=True
value2=False
print(value1 and value2)
print(value1 or value2)

#type conversion

a=23
b=int(4.78) #for type casting we have to write data type(value) like: int(b)
sum= a+b
print(sum)#will print the float value

#input syntax

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter the marks: "))

print(type(name), "Welcome", name)
print(type(age), "Your age is: ", age)
print(type(marks), "Your marks is: ", marks)