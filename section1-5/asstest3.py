#Numbers
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
print(5**2 * 4 + 1/4)

#Answer these 3 questions without typing code. Then type code to check your answer.
#What is the value of the expression 4 * (6 + 5)
print(4*(6+5))
#What is the value of the expression 4 * 6 + 5 
print(4*6+5)
#What is the value of the expression 4 + 6 * 5 
print(4+6*5)
#What is the type of the result of the expression 3 + 1.5 + 4?
print(type( 3 + 1.5 + 4))
#What would you use to find a number’s square root, as well as its square?
print(4**(1/2))
print(2**2)

#Strings
#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
print("hello"[1])
#Reverse the string 'hello' using slicing:
print("hello"[::-1])
#Given the string hello, give two methods of producing the letter 'o' using indexing.
print("hello"[4])
print("hello"[-1])

#Lists
#Build this list [0,0,0] two separate ways.
print([0]*3)
print([0,0,0])
#Reassign 'hello' in this nested list list3 = [1,2,[3,4,'hello']] to say 'goodbye' instead: 
list3 = [1,2,[3,4,'hello']]
list3[2][2] = "goodbye"
print(list3)
#Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#Dictionaries:
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d1 = {'simple_key':'hello'}
print(d1["simple_key"])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']["k2"])
d3= {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]["nest_key"][1][0])
d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d4['k1'][2]["k2"][1]["tough"][2][0])
#Can you sort a dictionary? Why or why not?: We can not sort dictionary because it was stick by key-value mà key thì là name do chúng ta đặt và nó không có thứ tự cụ thể

#Tuples:
#What is the major difference between tuples and lists? Các elemnt của Tuples là không thể reassign hay không thể immutable
#How do you create a tuple? Thêm data vào () ví dụ (1,2,3)

#Sets:
#What is unique about a set? Là các phần tử trong 1 set phải là duy nhất không có giá trị trùng lập nhau trong set đó
#Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

#Booleans:
#What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
#2>3 : False
#3 <= 2 : False
#3 == 2.0: False
#3.0 == 3: True
#4**0.5 != 2: False
#Final Question: What is the boolean output of the cell block below? 
# two nested lists 
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?  False
print(l_one[2][0] >= l_two[2]['k1'])
