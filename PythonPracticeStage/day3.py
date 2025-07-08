#string

str1="This is a string"
str2='This is a string'
str3="""TThis is a string"""
str4="for the , \nnext line"

print(str1)
print(str2)
print(str3)
print(str4)

#concatenation

print(str1 + str4)

#legth of the string

len1=len(str1)
print(len1)
print(len(str2))

#indexing

str5="walid"
ch= str5[4]
print(ch)

#slicing

w=str5[0:2]
print(w)

#str functions

str6="i am a coder"
print(str6.endswith("er"))
print(str6.capitalize())
print(str6.replace("r", "ing"))
print(str6.find("am"))
print(str6.count("coder"))

#conditional statement

age=17

if(age>=18):
    print("can vote")
elif(age<=22):
    print("cant smoke")