#Q1
movie = []
movie.append((input("Enter your first favorite movies: ")))
movie.append((input("Enter your second favorite movies: ")))
movie.append((input("Enter your third favorite movies: ")))
movie.sort()
print(movie)

#Q2:- check for palindrom
list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3]

copy1 = list1.copy()
copy1.reverse()

if(copy1 == list1):
    print("list is palindrom")
else:
    print("not palindrome")

copy2 = list2.copy()
copy2.reverse()

if(copy2 == list2):
    print("list is palindrom")
else:
    print("not palindrome")

#Q3 
grade = ('C', 'D', 'A', 'A', 'B', 'B', 'A',)
print("The number of A: ", grade.count('A'))

#Q4
grade = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
grade.sort()
print("The sorted list of the grades: ", grade)