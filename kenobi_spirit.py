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

def hello_world(): # hello world function that is created for the simulation game mystical fog!
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
    print("Welcome to the mystical journey!") # welcome Message

    # creating the prompt for the journey!
    print("You're on an enchanted journey and lost in the forrest of wonder. You see a mystical purple cat who strikes curiosity as he is enlightened by fireflies.\n\n")
    
    while True: # using a while loop to keep the loop going until the user responds with input
        print("What do you do?!") # the question to give input options for gameplay
        print("1. Meet the enlightened cat to see if you can possibly find an answer to get out of the forrest by crossing a bridge.") #Print option 1
        print("2. Stay where you're at.") # print option 2
        option1 = input("Choose option 1 or 2: ") # prompt user to enter one or two

        if option1 == "1": # if 1 was entered
            print("\n\n\nYou step onto the bridge to trust your new intuition as it leads you through the fog. A moment of truth as the bridge carries you to the orb of fireflies where the mystikal cat resides") # meet the mystikal cat through entering 1
            print("\n\nThat cat sees you and introduces herself as Mystikal Bean.") # the magikal Bean is a cat!
            print("\nThe Fireflies take you on the mystical journey to the top of the mountain where the ancient winds guide you in the Mystiks TeachingS!") # fireflies add to the story. I use print functions to prompt the user of the story and the game.
            break # break breaks out of the while loop into the next while loop.
        elif option1 == "2": # if two is pressed. The forest Lures the reader in!
            print("""
▄▄▄▄▄▄ .▄▄▄ .    ·▄▄▄    ▄▄▄ ▄▄▄ .▄▄ ▄▄▄▄▄     ▄▄▄▄• ▄▄▄▌ ▄▄▌ .▄▄ ·      ▄· ▄▌    ▄• ▄▌    ▪  ▐ ▄▄▄ 
•██ ██▪▐▀▄.▀·    ▐▄▄▪    ▀▄ █▀▄.▀▐█ ▀•██      ▐█ ▄█▪████• ██• ▐█ ▀.     ▐█▪██▪    █▪██▌    ██•█▌▐██▌
 ▐█.██▀▐▐▀▀▪▄    ██▪ ▄█▀▄▐▀▀▄▐▀▀▪▄▀▀▀█▐█.▪     ██▀█▌▐███▪ ██▪ ▄▀▀▀█▄    ▐█▌▐█▪▄█▀▄█▌▐█▌    ▐█▐█▐▐▐█·
 ▐█▌██▌▐▐█▄▄▌    ██▌▐█▌.▐▐█•█▐█▄▄▐█▄▪▐▐█▌·    ▐█▪·▐█▄█▐█▌▐▐█▌▐▐█▄▪▐█     ▐█▀·▐█▌.▐▐█▄█▌    ▐███▐█.▀ 
 ▀▀▀▀▀▀ ·▀▀▀     ▀▀▀ ▀█▄▀.▀  ▀▀▀▀ ▀▀▀▀▀▀▀     .▀   ▀▀▀.▀▀▀.▀▀▀ ▀▀▀▀       ▀ • ▀█▄▀▪▀▀▀     ▀▀▀▀ █▪▀ 
""") # the forest lures the reader in.
            print("\n\nYou take a step twoards the tunnel, but a ghost acts like the wind and sweeeps your off your feet!\nAll of a sudden you find yourself at the top of a mountain where the Fog is less, but you cannot see past the tree line below!")
            break # breaks out of the loop!
        else: # else is if niether one or two was entered for a message to do so for the user
            print("""
            
 ░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░▒▓████████▓▒░         ░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░        ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░        ░▒▓██████▓▒░  
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░        ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓█▓▒░             ░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░ 
                                                                                                                                                   
                                                                                                                                                   
\n\n""") # select 1 or 2 to continue the game!
    
    # printing to the story
    print("\nWell Done! you create your steps for intuition in the depths of an ancient forrest!! Here you get to fight for the forrests initiation!")
    while True: # The story progresses.
        print("You have a choice in instrument for this battle. You are ontop of the mountain where the spirit of the forrest has guided you!\nnow it is time to choose your intuitive weapon in which you will defeat the dark-worlds dragon!") # choose your wand!
        print("1. use the Star Fury. Defeat the dragon by fighting with the energy of the stars behind the great curtain of fog\n") # Star Fury uses the stars of the galaxy as moon energy radiates through the wand to fight the dragon
        print("2. use the Ancient Wand which uses the water and electrical Elements beneath the earth") # the ancient wand of the earth uses light energy and crystals to create the power of the wizard fighting the dragon!
        
        # The while loop has been a great deciding factor in the process of running an application.\n
        # the loop is continuous until stated otherwhise, in this case when 1 or 2 is pressed to proceed\n
        # to the next phase of the storyline. There is some more thought that can be carried out when thinking\n
        # about functions. But in my case currently I'm leaving the code leaping from one while loop to the next.\n
        # the if statement is stating if this option is chosen by the user print this, else if 2 is pressed print\n
        # the other version of the story. Where the else loop is looping back into the original while loop to re-iterate\n
        # the choices for the user to enter appropriately. Breaks in the code are for the option to print the actual statement\n
        # and break from the while loop allowing the program to go to the next while loop in the function. In this case there are\n
        # three while loops until the break of the loop is a break from the function to the end of the storyline.
        
        choice2 = input("Choose 1 or 2: ") # the choice is up to the person playing the game. Fight the dragon!
        
        # the input function is the python function that recieves input from the user. In this case choice2 is the input method as the input\n
        # of the user will be made to progress through the function. 
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
            break # break out of the loop
        elif choice2 == "2": # choice 2 prints good luck
            print("""

 ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             
 ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░ 
                                                                                                                                                     
""")
            break # break out of the while loop
        else: # type the correct input
            print("please select 1 or 2 to fight the DRAGON!") # printing a message for the user
            break # break from while loop to new loop of the game.


# Dragon Encounter
    while True:
        print("\nAs you continue, a massive dragon appears at the end of the road!") # storyline, the dragon and the wizard!
        print("What will you do?") # message from the cat!
        print("1. Walk away.") # don't walk away
        print("2. Fight the dragon!") # Fight the dragon!
        
        choice2 = input("Choose 1 or 2: ") # the choice is yours! user must enter 1 or 2

        if choice2 == "1": # game over if you choose 2
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
            print("You chose to walk away. The dragon roars as you fade into the fog. GAME OVER.") # Game Over
            break # break from loop to play again??
        elif choice2 == "2": # choice 2!
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
            print("\nYou raise your weapon, channeling its energy to face the dragon...") # you did it!
            print("With a final blast, you defeat the dragon and are transported to a new realm. Victory is yours!") # you faced the dragon!
            print("\nTHE END") # the end of the game should be a happy one, otherwise there's the new while loop to loop you back in to win!
            break # break out of this loop to the last loop
        else: # if the correct input is not created.
            print("Please choose 1 or 2.") # choose 1 or 2
# Ending Loop
    while True:
        replay = input("\nWould you like to play again? (yes/no): ").lower() # set all input to lowercase for program to read input yes or no
        if replay == "yes": # read yes
            print("\nRestarting the simulation...\n") # play again!
            hello_world() # calling on the games main function
        elif replay == "no": # replay input no?
            print("Thank you for playing! Goodbye.") # goodbye, best of luck next time!
            break # break out of the loop!
        else: # wrong input
            print("Invalid input, please type 'yes' or 'no'.") # type one or the other!


hello_world() # calling on the funciton to build each step of the simulation!
