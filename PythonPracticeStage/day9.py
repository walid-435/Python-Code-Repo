#File I/O - python can be used to perform operations on a file. (read & write)
#Text files - .txt, .docx, .log etc
#Binary files - .mp4, .mov, .png, .jpeg etc

#open, read & close file - 
#f = open ("file_name", "mode(r/w)")
f = open("D:\CodeDumpPython\PythonPracticeStage\demo.txt", "r")

#a = f.read - read and return the data of the file
data = f.read()
print(data)
f.close()