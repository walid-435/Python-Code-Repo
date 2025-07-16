#functions = block of statements that performs a specific task
#Syntax for creating functions - 
# def func_name(parameter1, parameter2 ...):
    #some work
    #return val
#Syntax for calling functions - func_name(arg1,  arg2 ...)
def calcSum(a, b):
    sum = a+b
    print(sum)
    
a = 5
b = 4
calcSum(a, b)

#type of functions = built in functions & user defined functions

#default arguments
def calcmul(a = 1, b = 1): #b, a=1
    mul = a*b
    print(mul)
    return mul
calcmul()

#recursion - when a function calls itself repeatedly
def rec_fact(n):
    if(n == 1 or n == 0):
        return 1
    return rec_fact(n-1)*n

n = int(input("enter the number for factorial: "))
print(rec_fact(n))