"""
Assignment Title: Text Based Game, Lab 4
Name: Uttam Dhamala
About Project:
            This is text based game. Program has 3 different functions.
            Players will be given different options to choose. Different
            functions will perform different task to give the result
            according to the player's choice. Program will take number of
            crew member as an input, and calculator imported from Survivor
            Calculator will calculate the percentage and number.
"""

import sys
from SurvivorCalculator import *


def play_gork():
    print("Welcome to Play Gork 1.0 \n"
          "Created by Uttam Dhamala \n")
    print("1. Play Gork")
    print("2. Exit")
    player_choice = int(input("Please choose your option here: "))
    if player_choice == 2:
        sys.exit()
    elif player_choice == 1:
        menu(welcome())
    else:
        print("Invalid Entry.")


def welcome():
    print("You are in charge of a top secret military mission when your \n"
          "space ship makes an emergency landing on the largest moon of \n"
          "planet Gork. The space ship is damaged. Oxygen levels in the \n"
          "space ship begin to drop.")
    number = int(input("How many personnel on the ship?: "))
    return number


def menu(number):
    print("What would you like to do? \n"
          "1. Attempt repairs on the ship. \n"
          "2. Request an emergency rescue from mission command. \n"
          "3. Break protocol and reveal the top secret space ship's location.")
    choice = int(input("Your choice: "))
    if choice == 1:
        print("Toxic material on the moon has corroded the launch gear \n"
              "and the launch exploded.")
    elif choice == 2:
        if number <= 4:
            print("Everybody was killed. No Survivors.")
            sys.exit()
        elif number > 4:
            percent_survived = calculatePct(number, 4)
            print("Oxygen was depleated before the rescue team arrived. \n"
                  "There were 4 people killed", percent_survived, "percentage of the personnel were rescued.")
    elif choice == 3:
        if number <= 4:
            print("Everybody was killed. No Survivors.")
            sys.exit()
        elif number > 4:
            number_survived = calculateTotal(number, 0.25)
            print("Russians agree to send a rescue ship, but secretly attempt to hack into the ships systems \n"
                  "remotely, which triggers an automatic shut down of all communications systems and locks all \n"
                  "mission critical storage units, including one of the storage unit that holds emergency oxygen tanks.\n"
                  "One quarter (.25) of all personnel are lost.", number_survived, "people survived.")
    else:
        print("You were eaten by a Grue")


play_gork()

"""
Sample Run
------Run with option 2 to exit from main menu.-------------
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/playGork/play_gork.py
Welcome to Play Gork 1.0 
Created by Uttam Dhamala 

1. Play Gork
2. Exit
Please choose your option here: 2

Process finished with exit code 0
------Run with option 1 to play from main menu with 8 personnel and option 1 from second menu-----
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/playGork/play_gork.py
Welcome to Play Gork 1.0 
Created by Uttam Dhamala 

1. Play Gork
2. Exit
Please choose your option here: 1
You are in charge of a top secret military mission when your 
space ship makes an emergency landing on the largest moon of 
planet Gork. The space ship is damaged. Oxygen levels in the 
space ship begin to drop.
How many personnel on the ship?: 8
What would you like to do? 
1. Attempt repairs on the ship. 
2. Request an emergency rescue from mission command. 
3. Break protocol and reveal the top secret space ship's location.
Your choice: 1
Toxic material on the moon has corroded the launch gear 
and the launch exploded.

Process finished with exit code 0

------Run with option 1 to play from main menu with 8 personnel and option 2 from second menu-----
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/playGork/play_gork.py
Welcome to Play Gork 1.0 
Created by Uttam Dhamala 

1. Play Gork
2. Exit
Please choose your option here: 1
You are in charge of a top secret military mission when your 
space ship makes an emergency landing on the largest moon of 
planet Gork. The space ship is damaged. Oxygen levels in the 
space ship begin to drop.
How many personnel on the ship?: 8
What would you like to do? 
1. Attempt repairs on the ship. 
2. Request an emergency rescue from mission command. 
3. Break protocol and reveal the top secret space ship's location.
Your choice: 2
Oxygen was depleated before the rescue team arrived. 
There were 4 people killed 0.5 percentage of the personnel were rescued.

Process finished with exit code 0

------Run with option 1 to play from main menu with 8 personnel and option 3 from second menu-----
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/playGork/play_gork.py
Welcome to Play Gork 1.0 
Created by Uttam Dhamala 

1. Play Gork
2. Exit
Please choose your option here: 1
You are in charge of a top secret military mission when your 
space ship makes an emergency landing on the largest moon of 
planet Gork. The space ship is damaged. Oxygen levels in the 
space ship begin to drop.
How many personnel on the ship?: 8
What would you like to do? 
1. Attempt repairs on the ship. 
2. Request an emergency rescue from mission command. 
3. Break protocol and reveal the top secret space ship's location.
Your choice: 3
Russians agree to send a rescue ship, but secretly attempt to hack into the ships systems 
remotely, which triggers an automatic shut down of all communications systems and locks all 
mission critical storage units, including one of the storage unit that holds emergency oxygen tanks.
One quarter (.25) of all personnel are lost. 6 people survived.

Process finished with exit code 0

------Run with option 1 to play from main menu with 2 personnel and option 2 from second menu for negative value----
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/playGork/play_gork.py
Welcome to Play Gork 1.0 
Created by Uttam Dhamala 

1. Play Gork
2. Exit
Please choose your option here: 1
You are in charge of a top secret military mission when your 
space ship makes an emergency landing on the largest moon of 
planet Gork. The space ship is damaged. Oxygen levels in the 
space ship begin to drop.
How many personnel on the ship?: 2
What would you like to do? 
1. Attempt repairs on the ship. 
2. Request an emergency rescue from mission command. 
3. Break protocol and reveal the top secret space ship's location.
Your choice: 2
Everybody was killed. No Survivors.

Process finished with exit code 0

------Run with option 1 to play from main menu with 2 personnel and option 3 from second menu for negative value----
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/playGork/play_gork.py
Welcome to Play Gork 1.0 
Created by Uttam Dhamala 

1. Play Gork
2. Exit
Please choose your option here: 1
You are in charge of a top secret military mission when your 
space ship makes an emergency landing on the largest moon of 
planet Gork. The space ship is damaged. Oxygen levels in the 
space ship begin to drop.
How many personnel on the ship?: 2
What would you like to do? 
1. Attempt repairs on the ship. 
2. Request an emergency rescue from mission command. 
3. Break protocol and reveal the top secret space ship's location.
Your choice: 3
Everybody was killed. No Survivors.

Process finished with exit code 0


"""
