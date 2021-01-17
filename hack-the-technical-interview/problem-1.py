# practice problem 1: fizzbuzz

# Write a function that takes a single input, a number, and prints out 1 through the number. If the number being printed is divisible by 3, print "Fizz" instead of the number itself. If the number being printed is divisible by 5 "Buzz". If the number being printed is divisible by 3 and 5, print "FizzBuzz."

# main function
def fizzBuzz(num):
  for x in range(1, num + 1):
    if x % 3 == 0 and x % 5 == 0: 
      # written this way instead of "x % 15" for the sake of readability
      print("FizzBuzz")
    elif x % 3 == 0:
      print("Fizz")
    elif x % 5 == 0:
      print("Buzz")
    else:
      print(x)

# testing
fizzBuzz(18)