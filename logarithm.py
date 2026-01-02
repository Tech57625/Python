import math

num = float(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    result = math.log(num)
    print(f"The natural logarithm of {num} is: {result}")
