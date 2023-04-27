print("Math Game !")
print()
multiple_no = int(input("Enter your multiple: "))

counter  = 0
for i in range(1, 11):
  answer = i * multiple_no
  print(i, "times", multiple_no)
  result = int(input("="))
  if result == answer:
    print("Well done! 😂😂" )
    counter += 1
  else:
    print("Sorry try again.")
  if counter == 10:
    print("congratulations. You made it.")
  else:
    print("Your score is ", counter, "out of 10 trials.")
