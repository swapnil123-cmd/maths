from math import sqrt
number=int(input("Enter a number: "))
if number>1:
  for i in range(2,int(sqrt(number))+1):
    if number % i == 0:
      print(number,": It is not a prime number")
      break
    else:
      print(number,": It is a prime number")
else:
  print("It is not a prime number")
      