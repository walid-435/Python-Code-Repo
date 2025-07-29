#File I/O - python can be used to perform operations on a file. (read & write)
#Text files - .txt, .docx, .log etc
#Binary files - .mp4, .mov, .png, .jpeg etc

#open, read & close file - 
#f = open ("file_name", "mode(r/w)")
f = open("D:\CodeDumpPython\PythonPracticeStage\demo.txt", "r")

#a = f.read - read and return the data of the file
data = f.read(5) #to read the first characters
line1 = f.readline() #to read a whole line
print(line1)
print(data)
f.close() 

#'r' = open for reading
#'w' = open for writting, truncating the file first
#'x' = create a new file and open it for writting
#'a' = open for writting, appending to the end of the file if it exists
#'b' = binary mode
#'t' = text mode
#'+' = open a disk file for updating
#'r+' = read + overwrite (pointer on start) - no truncate
#'w+' = read + overwrite - have truncate
#'a+' = read + append (pointer at end) - no truncate

#writting to a file
f = open("demo.txt", "w")
f.write("new line") #overwrites the entire file

f = open("demo.txt", "a")
f.write("new new line") #adds to the file

#with syntax - 
#with open("file name", 'mode') as f:
#       data = f.read()

#deleting a file - using the os module
#module - it's like a file written by another programmer that generally has a functions we can use
#module syntax - import 
#to intall new module - pip install name / pip3 install name (based on the python version)
import os

#file remove syntax - os.remove("filename")
os.remove()