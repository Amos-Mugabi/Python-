import os, time

todolist = []


def mylist():
  for items in todolist:
    print(items)


while True:
  menu = input(
    "To Do List Manager:\n Do you want to view, add, edit or remove an item from the to do list? "
  )
  if menu == "view":
    mylist()
  elif menu == "add":
    item = input("What do you want to add?")
    todol.append(item)
  elif menu == "remove":

    item = input("what do you want to remove?")
    checking = input("Are you sure you want to remove this?")
    if checking[0] == "yes":
      todolist.remove(item)
    mylist.remove()

    time.sleep(3)
    os.system("clear")
import os, time

todolist = []


def mylist():
  for items in todolist:
    print(items)


while True:
  menu = input(
    "To Do List Manager:\n Do you want to view, add, edit or remove an item from the to do list? "
  )
  if menu == "view":
    mylist()
  elif menu == "add":
    item = input("What do you want to add?")
    todol.append(item)
  elif menu == "remove":

    item = input("what do you want to remove?")
    checking = input("Are you sure you want to remove this?")
    if checking[0] == "yes":
      todolist.remove(item)
    mylist.remove()

    time.sleep(3)
    os.system("clear")

