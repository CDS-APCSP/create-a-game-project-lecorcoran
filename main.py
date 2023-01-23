import os, time
import random

health = 100
gun = random.choice([True, False])
explosives = random.choice([True, False])

def startGame():
  os.system('clear')
  print("Welcome soldier. Your name is Lieutenan Barnes, and   you are about to storm the Omaha Beach in Normandy, France.")
  print()
  print("Let's go soldier.")
  time.sleep(5)
  choice1()

def choice1():
  global gun
  os.system('clear')
  if gun == True:
    print("You gear up and leave the boat with your M1 Gerand")
    time.sleep(3)
    choice2()
  else:
    leave = input("You are about to leave the boat. There is an M1 Gerand on the ground. Would you like to pick it up?")
    if (leave == "yes"):
      print("You pick up the gun and leave the boat.")
      time.sleep(3)
      choice2()
    elif (leave == "no"):
      print("You leave the boat without a gun")
      time.sleep(3)
      choice2()
    else:
      print("Sorry, that command is not found")
      time.sleep(3)
      choice1()

def choice2():
  global explosives, health
  os.system('clear')
  print("After leaving the boat you sprint through the water as machine gun rounds fly by you on all sides.")
  print()
  direction = input("Do you go left and duck behind a tank to catch your   breath, or sprint forward toward the next cover?")
  if (direction == "left"):
    os.system('clear')
    print("You make it to the tank and catch your breath.")
    time.sleep(3)
    grenade()
  elif (direction == "forward"):
    os.system('clear')
    print("As you valiantly sprint forward for your life trying  to advance to the next cover, you get sniped through your chest.")
    time.sleep(5)
    death()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    choice2()

def grenade():
  global explosives, health
  os.system('clear')
  print("As you sit behind the tank, you check yourself for any explosives.")
  time.sleep(3)
  os.system('clear')
  if explosives == True:
    print("You find a grenade or you back pouch. You decide to throw it hard up the clif.")
    time.sleep(3)
    print("BOOOOM! You throw it right into the bunker and take out everyone inside!")
    print("With your adrenaline rush you stand up and run towards the next cover you can see.")
    time.sleep(5)
    choice3()
  else:
    print("You don't find any explosives on you so you decide to advance forward and not stay a sitting duck.")
    time.sleep(3)
    choice3()
  
def choice3():
  global explosives, health
  os.system('clear')
  print("As you get up and start running, you see your platoon leader and others full out sprinting towards a sand   dune with a lot of cover. He shouts at you to follow  them, but you feel really scared running out in the open, but you must make a split second decision.")
  print()
  decision = input("Do you 'go with', or 'go left' towards cover?")
  if decision == "go with":
    os.system('clear')
    print("You go with the group and run for your life toward the sand dune. You survive as you dive into cover.")
    time.sleep(3)
    choice4()
  elif decision == "go left":
    os.system('clear')
    print("As you go left toward the nearest cover, you step on a mine and get blow to bits.")
    time.sleep(3)
    death()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    choice3()

def choice4():
  global explosives, health
  os.system('clear')
  print("You talk with your platoon leader and he instructs everyone waiting in cover to get up and push when he calls. Everyone reloads and prepares themselves for this death press. '3, 2, 1, GO!' he calls, and everyone get up and sprints toward the German bunkers.")
  time.sleep(3)
  print()
  print("You run up the hill with your comrades, and you and a few others stop at the first German bunker, as you slowly approach an enemy grenade rolls out.")
  bunker = input("Do you 'jump' on the grenade as an attempt to save your fellow soldiers, or do you 'yell' grenade and dive away from it to try and escape it?")
  if bunker == "jump":
    os.system('clear')
    print("You jump on the active grenade and sacrifice yourself as it blows up, saving all of the soldiers and friends standing behind you")
    time.sleep(3)
    death()
  elif bunker == "yell":
    os.system('clear')
    print("You save yourself by diving away from the grenade as it explodes, killing a few men around you")
    time.sleep(2)
    print()
    print("There is no time to mourn their loss though, as one of your fellow soldiers with a blowtorch goes into the bunker and incinerates everything in there.")
    time.sleep(2)
    print()
    print("After that bunker you move to the top of the hill where everyone has gathered after clearing the bunkers. You live another day as you and your brother push into Normandy and elimate the Nazis one by one")
    time.sleep(5)
    endGame()
          
def death():
  os.system("clear")
  print("You have passed away, but you will always be remembered amongst the heroes who sacrificed their lives on this day.")
  endGame()
          
def endGame():
  os.system("clear")
  pass

startGame()