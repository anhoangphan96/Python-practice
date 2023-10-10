import math
import string
#Complete the following questions: ____ Write a function that computes the volume of a sphere given its radius.
#The volume of a sphere is given as
def vol(rad):
    return (4/3* math.pi * (rad**3))
print(vol(2))

#Write a function that checks whether a number is in a given range (inclusive of high and low)\
def ran_bool(num,low,high):
  return low <= num <= high
print(ran_bool(3,1,10))


#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
#HINT: Two string methods that might prove useful: .isupper() and .islower()
#If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
  upper_ammount = 0
  lower_ammount = 0
  for w in s:
    if w.isupper():
      upper_ammount += 1
    elif w.islower():
      lower_ammount += 1  
  print(f"No. of Upper case characters :  {upper_ammount}")
  print(f"No. of Lower case Characters :  {lower_ammount}")
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
  return list(set(lst))
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#Write a Python function to multiply all the numbers in a list.
#Sample List : [1, 2, 3, -4]
#Expected Output : -24

def multiply(numbers):  
  multiplyn = 1
  for n in numbers:
    multiplyn *= n
  return multiplyn

print(multiply([1, 2, 3, -4]))


#Write a Python function that checks whether a word or phrase is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
def palindrome(s):
  trim_s = s.replace(" ", "")
  if trim_s == trim_s[::-1]:
    return True
  else:
    return False

print(palindrome("helleh"))


#Hard:
#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
#Hint: You may want to use .replace() method to get rid of spaces.
#Hint: Look at the string module
#Hint: In case you want to use set comparisons
def ispangram(str1, alphabet=string.ascii_lowercase):
  list_str1 = list(set(list(str1.replace(" ","").lower())))
  list_str1.sort()
  if list_str1 == list(alphabet):
    return True
  else:
    return False
print(ispangram("The quick brown fox jumps over the lazy dog"))
  
  
