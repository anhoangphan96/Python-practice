#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(numbs):
  count = 0
  for num in numbs:
    if num != 7: 
      if num ==0:
        count = count + 1
      else:
        continue
    else:
      if num == 7 and count != 2:
        return False
      else:
        return True
print(spy_game([1,2,4,0,0,7,5]))
print( spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.

def count_primes(num):
  primes=[2]
  x = 3
  while x < num:
    for y in range(3,x,2):
      if x%y == 0:
        x += 2
        break
    else:
      primes.append(x)
      x+=2
  return len(primes)
print(count_primes(100))
print(list(range(3,9,2)))


