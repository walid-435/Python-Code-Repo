#Q1 - Create a new file and input lines
with open("practicefile.txt", 'w') as f:
    f.write("Hi everyone, \n we are learning file i/o \n using java. \n I like programming in java")
    
#Q2 - Change java to python in the files
with open("practicefile.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("java", "Python")
print(new_data)

with open("practicefile.txt", "w") as f:
    f.write(new_data)
    
#Q3 - search "learning" exists or not
with open("practicefile.txt", "r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("found")
    else:
        print("not found")
        
#Q4 - find the line in which the word "learning" occur first
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practicefile.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
        
check_for_line()

#Q5 - file containg numbers separated by comma, print the count of even numbers
with open ("practicefile.txt", "r") as f:
    data = f.read()
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
    
    if(data[i] % 2 == 0):
        print()
        
#OR

count = 0
with open("practicefile.txt") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1

print(count)