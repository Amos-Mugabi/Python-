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

   name = input("Name your legend:")
   character = input("Character Type(Human, Elf, Wizard, Orc):\n ")
   if name == "Amos" and character == "Human":
    print("Health: ", health())
    print("STRENGTH: ", strength())
    print()

    again = input("Again: ")
    if again == "No":
      break
    time.sleep(1)
    os.system("clear")

  
  



  
