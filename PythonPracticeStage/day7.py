#loops
#while condition :
    #work for the loop

count = 5
while count <= 5:
    print("hello")
    count +=1

print(count)

#break = used to terminate the loop when encountered

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
a = 36
index = 0
while index < len(tup):
    if(tup[index] == a):
        print("element found at index: ", index)
        break;
    else:
        print("element not found.")
    index+=1

#continue = terminates the execution in the current iteration and continues execution of the loop with the next iteration. (works as skip)
#odd
i = 0
while i<= 10:
    if(i%2 == 0):
        i+=1
        continue
    print(i)
    i+=1
  
#even  
i = 0
while i <= 10:
    if(i%2 != 0):
        i+=1
        continue
    print(i)
    i+=1
    
#for loop : used for sequntial travarsal of group list, string, tuples
#for element=(any variable) in list=(mentioned list):
        #work for loop

#for char=(any variable) in str=(mentioned string):
        #work for loop

nums = [1, 2, 3, 4]
for i in nums:
    print(i)
        
#for loop with else = 
#for element (any avariable) in list=(mentioned list):
        #work for loop
#else:
        #work when loop ends
        
nums = [1, 2, 3, 4]
for i in nums:
    print(i)
else:
    print("end")
    
#range = it returns a sequence of numbers, starting from 0 (by default) and increments by 1 (by default) and stops before a specified number.
#rage based on  - start=0, step=1, end=5 So, range will be range(5)= 0,1,2,3,4
#syntax = range(start?(optional), stop, step?(optional))
range(5)
for i in range(5):
    print(i)
    
#even
for i in range(2, 100, 2):
    print(i)
    
#odd
for i in range(1, 100, 2):
    print(i)
    
#pass = it is null statement that does nothing. mainly used as a future code placeover
for i in range(5):
    pass

print("something")