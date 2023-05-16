print("\033[33m","Super Subroutine")
print()
print("With my",  "\033[0;35m", "new program I can","\033[33m", "just call red","\033[0;31m", "and", "\033[33m", "that word will appear in the color I set it to.")
print()
print("\033[33m","With no weird gaps.", "\033[33m")
print()
print("Epic")

word = input("Enter a word: ")
color = input("Enter a color: ")
if color=="red":
    print("\033[31m", word, sep="", end="")
   


