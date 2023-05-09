import random
print("Infinity Dice 🧊")

sides = int(input("How many sides?: "))
again = "yes"
def rollDice(sides):
  print("You rolled", random.randint(1, sides) )
  
while again == "yes":
    rollDice(sides)
    again = input("Roll again?")
