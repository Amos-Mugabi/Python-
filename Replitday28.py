import os, time, random


print("Character Builder.")


def sided_dice(side):
  dice_stat = random.randint(1, side)
  return dice_stat

def health():
  health_stat = ((sided_dice(6) * sided_dice(12))/2) + 10
  return health_stat
def strength():
  strength_stat = ((sided_dice(6) * sided_dice(8))/2) + 12
  return strength_stat
  
while True:


  
  name1 = input("Name your legend:")
  character1 = input("Character Type(Human, Elf, Wizard, Orc):\n ")
  print(name1)
  name1 = health1()
  character1 = strength1()
  print("Health: ", health1())
  print("STRENGTH: ", strength1())
  print()
  name2 = input("Name your legend:")
  character2 = input("Character Type(Human, Elf, Wizard, Orc):\n ")
  name1 = health2()
  character1 = strength2()
  print("Health: ", health2())
  print("STRENGTH: ", strength2())
  print()


     
    again = input("Again: ")
    if again == "No":
      break
    time.sleep(1)
    os.system("clear")

  
  



  
