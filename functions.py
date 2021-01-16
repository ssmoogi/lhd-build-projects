my_name = "Sahana"

def say_hello(name):
  print("Hi, " + name)
  # print("Hi, {}".format(name))
  
say_hello(my_name)
say_hello("Mara")
say_hello("Rida")

def two_hellos(firstName, secondName):
  print(firstName + " says hello to " + secondName)
  
two_hellos("Lily", "Elias")

def multiply_numbers(num_one, num_two):
  # print(num_one * num_two)
  num_three = num_one * num_two
  print(num_three)
  
multiply_numbers(6, 4)