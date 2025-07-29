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