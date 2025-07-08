#list in python

marks=[34, 213, 1654, 567]
print(marks)
print(type(marks)) #to print the type of the list
print(len(marks)) #to print the length of the list
print(marks[3]) #to print single index

student=["walid", 435, "Uttara"] #list can save different types of data at a time & can be changed anytime

student[0]="Walid"
print(student)

#sublisting 
#list_name [start ind : ending ind] (ending index will not be included in this case)

print(marks[1:4])
