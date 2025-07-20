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