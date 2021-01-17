# practice problem 2: string rotation

# Write a function that takes in two string inputs, and returns true if they are a rotation of each other.


# solution 1
def rotate1(string, candidate, stop=""):
    if string == candidate:
      return True
    if candidate == stop:
      return False
    if not stop:
      stop == candidate
    rot = candidate[1:] + candidate[0]
    return rotate1(string, rot, stop)

print(rotate1("ABCD", "CDAB"))

# solution 2
def rotate2(original, candidate):
    return len(original) == len(candidate) and candidate in original * 2

print(rotate2("ABCD", "BCDA"))
