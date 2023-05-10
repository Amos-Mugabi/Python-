import random
print("Character Stats Generator.")
print()
def rolldice(sides):
  stat = random.randint(1, sides)
  return stat




def rolldice2_and_8():
  roll_6 = rolldice(6)
  roll_8 = rolldice(8)

  health = roll_6 * roll_8
  return health

print()


newcharacter = "yes"

while newcharacter == "yes":
  name = input("Name your warrior: ")
  health = str(rolldice2_and_8())
  print("Their health is ", health, "hp")

newcharacter = input("Do you want another character? ")

