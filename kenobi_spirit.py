#!/usr/bin/env python3
"""
Creating a simulation App!
The simulation was created using VIM with Ubuntu.
The reason why is because if one chooses to use VS Code
the syntax is in a DOS implementation which has white space
dependencies added to the format of the script where the
hidden syntax of new lines and etc are hidden which the
python interpreter reads as errors. If this happens someone
can simply use <pip install dos2unix> as a command and re-organize
their script using <dos2unix filename> to fix the issue.

the resource as an exmaple of this type of story-telling can be
seen here --> https://thewisesloth.com/2017/10/18/7-choose-your-own-adventure-templates-and-prompts/

enjoy!
"""

def hello_world():
    print("""
 _______           _______ __________________ _______  _______  _          _______  _______  _______ 
(       )|\     /|(  ____/ /__   __//__   __/(  ____ \(  ___  )( \        (  ____ \(  ___  )(  ____ /
| () () |( \   / )| (    \/   ) (      ) (   | (    \/| (   ) || (        | (    \/| (   ) || (    \/
| || || | \ (_) / | (_____    | |      | |   | |      | (___) || |        | (__    | |   | || |      
| |(_)| |  \   /  (_____  )   | |      | |   | |      |  ___  || |        |  __)   | |   | || | ____ 
| |   | |   ) (         ) |   | |      | |   | |      | (   ) || |        | (      | |   | || | \_  )
| )   ( |   | |   /\____) |   | |   ___) (___| (____/\| )   ( || (____/\  | )      | (___) || (___) |
|/     \|   \_/   \_______)   )_(   \_______/(_______/|/     \|(_______/  |/       (_______)(_______)
                                                                                                     
""")
    print("Welcome to the mystical journey!")

    # creating the prompt for the journey!
    print("You're on an enchanted journey and lost in the forrest of wonder. You see a mystical purple cat who strikes curiosity as he is enlightened by fireflies.\n\n")
    
    while True:
        print("What do you do?!")
        print("1. Meet the enlightened cat to see if you can possibly find an answer to get out of the forrest by crossing a bridge.")
        print("2. Stay where you're at.")
        option1 = input("Choose option 1 or 2: ")

        if option1 == "1":
            print("\n\n\nYou step onto the bridge to trust your new intuition as it leads you through the fog. A moment of truth as the bridge carries you to the orb of fireflies where the mystikal cat resides")
            print("\n\nThat cat sees you and introduces herself as Mystikal Bean.")
            print("\nThe Fireflies take you on the mystical journey to the top of the mountain where the ancient winds guide you in the Mystiks TeachingS!")
            break
        elif option1 == "2":
            print("""
▄▄▄▄▄▄ .▄▄▄ .    ·▄▄▄    ▄▄▄ ▄▄▄ .▄▄ ▄▄▄▄▄     ▄▄▄▄• ▄▄▄▌ ▄▄▌ .▄▄ ·      ▄· ▄▌    ▄• ▄▌    ▪  ▐ ▄▄▄ 
•██ ██▪▐▀▄.▀·    ▐▄▄▪    ▀▄ █▀▄.▀▐█ ▀•██      ▐█ ▄█▪████• ██• ▐█ ▀.     ▐█▪██▪    █▪██▌    ██•█▌▐██▌
 ▐█.██▀▐▐▀▀▪▄    ██▪ ▄█▀▄▐▀▀▄▐▀▀▪▄▀▀▀█▐█.▪     ██▀█▌▐███▪ ██▪ ▄▀▀▀█▄    ▐█▌▐█▪▄█▀▄█▌▐█▌    ▐█▐█▐▐▐█·
 ▐█▌██▌▐▐█▄▄▌    ██▌▐█▌.▐▐█•█▐█▄▄▐█▄▪▐▐█▌·    ▐█▪·▐█▄█▐█▌▐▐█▌▐▐█▄▪▐█     ▐█▀·▐█▌.▐▐█▄█▌    ▐███▐█.▀ 
 ▀▀▀▀▀▀ ·▀▀▀     ▀▀▀ ▀█▄▀.▀  ▀▀▀▀ ▀▀▀▀▀▀▀     .▀   ▀▀▀.▀▀▀.▀▀▀ ▀▀▀▀       ▀ • ▀█▄▀▪▀▀▀     ▀▀▀▀ █▪▀ 
""")
            print("\n\nYou take a step twoards the tunnel, but a ghost acts like the wind and sweeeps your off your feet!\nAll of a sudden you find yourself at the top of a mountain where the Fog is less, but you cannot see past the tree line below!")
            break
        else:
            print("""
            
 ░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░▒▓████████▓▒░         ░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░        ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░        ░▒▓██████▓▒░  
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓█▓▒░             ░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░ 
                                                                                                                                                   
                                                                                                                                                   
\n\n""")
    
    # printing to the story
    print("\nWell Done! you create your steps for intuition in the depths of an ancient forrest!! Here you get to fight for the forrests initiation!")
    while True: # The story progresses.
        print("You have a choice in instrument for this battle. You are ontop of the mountain where the spirit of the forrest has guided you!\nnow it is time to choose your intuitive weapon in which you will defeat the dark-worlds dragon!")
        print("1. use the Star Fury. Defeat the dragon by fighting with the energy of the stars behind the great curtain of fog\n")
        print("2. use the Ancient Wand which uses the water and electrical Elements beneath the earth")
        """
        The while loop has been a great deciding factor in the process of running an application.\n
        the loop is continuous until stated otherwhise, in this case when 1 or 2 is pressed to proceed\n
        to the next phase of the storyline. There is some more thought that can be carried out when thinking\n
        about functions. But in my case currently I'm leaving the code leaping from one while loop to the next.\n
        the if statement is stating if this option is chosen by the user print this, else if 2 is pressed print\n
        the other version of the story. Where the else loop is looping back into the original while loop to re-iterate\n
        the choices for the user to enter appropriately. Breaks in the code are for the option to print the actual statement\n
        and break from the while loop allowing the program to go to the next while loop in the function. In this case there are\n
        three while loops until the break of the loop is a break from the function to the end of the storyline.
        """
        choice2 = input("Choose 1 or 2: ")
        """
        the input function is the python function that recieves input from the user. In this case choice2 is the input method as the input\n
        of the user will be made to progress through the function. 
        """
        if choice2 == "1": # I use the == sign because it is equal+to and the input of the user.
            print(""" 

 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░░▒▓██████▓▒░▒▓████████▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                    
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░           ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░ 
                                                                                                                                                            
                                                                                                                                                            
""")
            break
        elif choice2 == "2":
            print("""

 ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             
 ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
                                                                                                                                                     
""")
            break
        else:
            print("please select 1 or 2 to fight the DRAGON!")
            break


# Dragon Encounter
    while True:
        print("\nAs you continue, a massive dragon appears at the end of the road!")
        print("What will you do?")
        print("1. Walk away.")
        print("2. Fight the dragon!")
        
        choice2 = input("Choose 1 or 2: ")

        if choice2 == "1":
            print("""
=============================================================================
=  ====  ===    ===  ====  =====  =========    =====    ====      ==        =
=   ==   ==  ==  ==  ====  =====  ========  ==  ===  ==  ==  ====  =  =======
==  ==  ==  ====  =  ====  =====  =======  ====  =  ====  =  ====  =  =======
==  ==  ==  ====  =  ====  =====  =======  ====  =  ====  ==  ======  =======
===    ===  ====  =  ====  =====  =======  ====  =  ====  ====  ====      ===
====  ====  ====  =  ====  =====  =======  ====  =  ====  ======  ==  =======
====  ====  ====  =  ====  =====  =======  ====  =  ====  =  ====  =  =======
====  =====  ==  ==   ==   =====  ========  ==  ===  ==  ==  ====  =  =======
====  ======    ====      ======        ===    =====    ====      ==        =
=============================================================================
                    """)
            print("You chose to walk away. The dragon roars as you fade into the fog. GAME OVER.")
            break
        elif choice2 == "2":
            print("""
=========================================================================
=  ====  ===    ===  ====  =====  ====  ====  =    =  =======  =  =  =  =
=   ==   ==  ==  ==  ====  =====  ====  ====  ==  ==   ======  =  =  =  =
==  ==  ==  ====  =  ====  =====  ====  ====  ==  ==    =====  =  =  =  =
==  ==  ==  ====  =  ====  =====  ====  ====  ==  ==  ==  ===  =  =  =  =
===    ===  ====  =  ====  =====   ==    ==  ===  ==  ===  ==  =  =  =  =
====  ====  ====  =  ====  ======  ==    ==  ===  ==  ====  =  =  =  =  =
====  ====  ====  =  ====  ======  ==    ==  ===  ==  =====    ==========
====  =====  ==  ==   ==   =======    ==    ====  ==  ======   =  =  =  =
====  ======    ====      =========  ====  ====    =  =======  =  =  =  =
=========================================================================
""")
            print("\nYou raise your weapon, channeling its energy to face the dragon...")
            print("With a final blast, you defeat the dragon and are transported to a new realm. Victory is yours!")
            print("\nTHE END")
            break
        else:
            print("Please choose 1 or 2.")
# Ending Loop
    while True:
        replay = input("\nWould you like to play again? (yes/no): ").lower()
        if replay == "yes":
            print("\nRestarting the simulation...\n")
            hello_world()
        elif replay == "no":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")


hello_world() # calling on the funciton to build each step of the simulation!
