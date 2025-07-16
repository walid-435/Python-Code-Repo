#Q1 - WAF to print the length of a list
def prinlen(n):
    list = []
    for i in range(n):
        l = int (input("enter number for list: "))
        list.append(l)
        i+=1
    print(list)
    print(len(list))
        
n = int(input("enter the size for the list: "))
prinlen(n)

#Q2 - WAF to print the elements of a list in a single line. (list parameter)
list2 = ["Mohammad", "Walid", "Rahman"]

def single_line(list2):
    print(list2[0], end = " ")
    print(list2[1], end = " ")
    print(list2[2], end = " ")
    return

single_line(list2)

#Q3 - WAF to find the factorial of n. (n parameter)
def find_fac(n):
    fac = 1
    for i in range(1, n+1):
        fac*=i
    print(fac)

n = int(input("enter a number: "))
find_fac(n)

#Q4 - WAF to convert USD to TK
def con_currency(amt):
    USD = 122.30
    TK = USD * amt
    print("TK", TK)

amt = int(input("enter the amount of USD: $"))
con_currency(amt)

#H.Q - WAF to return odd even
def odd_even(n):
    if(n%2 == 0):
        print("Number is even")
    else:
        print("Number is odd")

n = int(input("enter a number: "))
odd_even(n)

#Q5 - WARF to calculate the sum of the first n natural numbers
def calc_sum(n):
    if(n == 0):
        return 0
    print(n)
    return calc_sum(n-1) + n

n = int(input("enter a number: "))
sum = calc_sum(n)
print(sum)

#Q6 - WARF to print all elements in a list
def prin_list(list, index = 0):
    if(index == len(list)):
        return
    print(list[index])
    prin_list(list, index+1)
fruits = ["apple", "banana", "mango"]
prin_list(fruits)