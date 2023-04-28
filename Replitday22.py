import random
counter = 0
print("Totally Random One-Million-to-One")

while True:
  number = int(input("What is your guess?: "))
  if number <= 500000:
    print("Too low.")
  elif number >= 700000:
    print("Too high.")
  elif number == 650000:
    print("Correct! ")
    break
  else:
    print("Sorry try again.")

    print("It took you 4 guesses to get the number correct.")
    print("Click 'run' to try again with a different number.")
