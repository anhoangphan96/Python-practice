
#Advanced Numbers
#Problem 1: Convert 1024 to binary and hexadecimal representation
print(bin(1024))
print(hex(1024))
#Problem2: Round 5.232222 to two decimal places
print(round(5.23222,2))


#Advanced Strings
#Problem3: Cehck if every letter in the string s is lowercase
s = "hello how are you Mary, are you feeling okay?"
print(s.islower())

#Problem4: How many times does the letter("w") show yp in the string below?

s="twywywytwewewfhdhfvdhfvwwwwaaaa"
print(s.count("w"))


#Advanced Sets
#Problem 5: Find the elements in sét that are not in set2
set1 ={2,3,1,5,6,8}
set2 ={3,1,7,5,6,8}
print(set1.difference(set2))
#Problem6: Find all elemets that are in eirther set:
print(set1.union(set2))

#Advanced Dictionaries
#Problem 7: create this dictionary: {0:0, 1:1, 2:8, 3:27, 4:64} using dictionary comprehension

print({x:x**3 for x in range(5)})

#Advanced Lists
#Problem 8: Reverse the list below:

l=[1,2,3,4]
l.reverse()
print(l)
#Problem 9: sort the list below:
l2=[3,4,5,2,1]
l2.sort()
print(l2)
