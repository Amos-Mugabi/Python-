print("star Wars Name Generator.✨")
print()
name1 = input(f"Input your first name > ")
name2 = input("Input your last name > ")
name3 = input("Input your mother`s maiden name > ")
city = input(" Input the city where you were born > ")
print(f"Your Star Wars name is ", {name1[:3].title()},
      {name2[:3].strip().lower()}, {name3[:2].strip().title()},
      {city[-3:].strip().lower()})


