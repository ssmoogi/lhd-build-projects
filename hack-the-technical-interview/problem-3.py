# practice problem 3: zig-zag arrays

# Write a function that takes an array with distinct elements and sorts them in a zig-zag fashion.

# my solution (doesn't work :'))

''' def zigzag(arr):
  zigged = []
  arr.sort()
  for i in arr:
    zigged.append(arr[0])
    zigged.append(arr[-1])
    arr = arr[1:(len(arr)-1)]
  print(zigged)

zigzag([1, 4, 3, 2]) '''

# solution 1

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

def zigzag1(arr):
  srt = sorted(arr)
  left = 1
  while left < len(srt) -1:
    swap(srt, left, left + 1)
    left = left + 2
  print(srt)

zigzag1([1, 4, 3, 2])

# solution 2

def zigzag2(arr):
  flag = True
  n = len(arr)
  for i in range(n-1):
    if flag is True:
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
      if arr[i] < arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
    flag = bool(1 - flag)
  print(arr)

zigzag2([1, 4, 3, 2])