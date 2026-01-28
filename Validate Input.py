y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!") 