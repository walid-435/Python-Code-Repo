#dictionary = used to store data values in key:value pairs (unorderd, mutable & don't allow the duplicate keys)

info = {    
    "name" : "Mohammad Walid Rahman",
    "age" : 22,
    "address" : "Dhaka",
    "university" : "Daffodil International University",
    "phone_number" : 1234,
    "subjects" : ["SWE", "CSE", "CSC"]
}

print(info)
info["name"] = "Walid" #assign new value to the key
print(info["name"])

#nested dictionary

student = {
    "name" : "Walid",
    "subjects" : {
        "phy" : 90,
        "chem" : 80,
        "bio" : 95
    }
}

print(student)
print(student["subjects"]["chem"])

#methods of dictionary
#myDict.keys() = returns all key

print(len(student)) #amount of keys
print(student.keys())
print(list(student.keys())) #to get the values in a list

#myDict.values() = returns all values

print(student.values())

#myDict.items() = returns all (key, values) pairs as tuples

print(student.items())

#myDict.get("keys") = returns the keys according to the value

print(student.get("subjects"))

#myDict.update(newDict) = inserts specified items to the dictionary

new = {
    "area" : "Uttara"
}
student.update(new)
student.update({"city" : "Dhaka"})
print(student)

#sets = collection of unordered items (each element must be unique and immutable)
#null set syntax = null_set = set()

collection = {1, 3, 4, 3, "hey", "hello"}
print(collection)
print(type(collection))

#set methods
#set.add(element) = adds element 

empty = set()
empty.add(1)
empty.add("hello")
empty.add(2)
print(empty)

#set.remove(element) = removes the element

empty.remove("hello")
print(empty)

#set.clear() = clears the set

empty.clear()
print(empty)

#set.pop() = removes a random value

empty.pop()
print(empty)

#set.union(set2) = combines both set values & returns a new set

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print(set1.union(set2))

#set.intersection(set2) = combines common values & return new values in a set

print(set1.intersection(set2))