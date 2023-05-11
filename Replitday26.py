from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    play_back = int(input("Press 2 anytime to stop  playback and go back to the menu: "))
    
    if play_back == "2":
      source.paused = True
      return
    else:
      continue
      
      

while True:
  # clear the screen 
  #time.sleep()
  os.system("clear")
  print("MyPOD Music Player")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to exit")
  time.sleep(2)
  print("Press anything else to see the menu again.")
  
  
  play = int(input("Press 1 to Play: "))
  if play == "1": 
      print("Now playing your favourites.")
  
  elif play == "2":
    exit()
  else:
    continue
