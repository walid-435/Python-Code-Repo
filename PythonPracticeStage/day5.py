#list methods
#list.append() = adds one element at the end of the list

list = [3, 2 , 1]
list.append(4)
print(list)

#list.sort() = sorts in ascending order

list.sort()
print(list)

#list.sort(reverse=True) = sorts in decending order

list.sort(reverse = True)
print(list)

#list.reverse() = reverses the list

list.reverse()
print(list)

#list.insert(index, element) = inserts element at index

list.insert(1, 5)
print(list)

#list.remove() = removes the first occurrence of the element

list.remove(2)
print(list)

#list.pop(index) = removes the element at index

list.pop(2)
print(list)

#tuples = a built in data-type which let us create immutable sequences of values
#syntax = {name = (your stuffs,)}

tup = (1, 2, 3,)
print(tup)
print(type(tup))

#slicing

print(tup[1:3])

#tuple methods
#tup.index(element) = provides the index of the first occurrence

a = ('b', 'c', 'd', 'd', 'e',)
print(a.index('e'))

#tup.count(element) = counts the total occurences

print(a.count('d'))