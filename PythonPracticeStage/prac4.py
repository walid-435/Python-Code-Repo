#Q1 - store word meanings
dict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}

print(dict)

#Q2 - find the number of classroom
subject = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print(len(subject))

#Q3 - take input of 3 subjects marks in a dictionary
marks = {}
m1 = int(input("Enter the marks for physics: "))
m2 = int(input("Enter the marks for chemistry: "))
m3 = int(input("Enter the marks for maths: "))

marks.update({"physics" : m1})
marks.update({"chemistry" : m2})
marks.update({"maths" : m3})

print(marks)

#Q4 - save 9 & 9.0 in a set
values = {
    ("int", 9),
    ("float", 9.0)
}

value = {9, "9.0"}

print(values)