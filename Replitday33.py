
print("To Do List Manager:")
print()

todolist = [ ]

def mylist():
  for item in todolist():
    print(item)
    

while True:
  action = input("Do you want to view, add or edit your to do list? ")
  if action == "view":
    mylist()
  elif action == "add":
    item = input("What do you want to add?")
    todolist.append(item)
  elif action == "edit":
    item = input("What do you want to remove?")
    todolist.remove(item)







    
