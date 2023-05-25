
namelist = []
print()


def peopleslist():
  print()


for item in namelist:
  print(item)
print()

while True:
  fname = input("Enter your first name: ").strip().capitalize()

  lname = input("Enter your last name: ").strip().capitalize()
  item = f"{fname}{lname}"
  if item not in namelist:
    namelist.append(item)
  else:
    print("Sorry, Try again.")
  peopleslist()

