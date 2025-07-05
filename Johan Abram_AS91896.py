import random
import msvcrt

def game():

    # Prints welcome message
    print("""\033[96m
  ____       _        _                         
 |  _ \ ___ | | _____| |_ _ __ ___   ___  _ __  
 | |_) / _ \| |/ / _ \ __| '_ ` _ \ / _ \| '_ \ 
 |  __/ (_) |   <  __/ |_| | | | | | (_) | | | |
 |_|   \___/|_|\_\___|\__|_| |_| |_|\___/|_| |_|                                             
\033[0m""")

    # Introduction and trainer name input
    print("Welcome to Pokétmon Adventure!")
    trainer_name = input("\033[1;97mTo start please enter your trainer name: \033[0m")
    print(f"\nWelcome, trainer {trainer_name}! Let's start your Pokétmon adventure!")
    print("You wake up in Paimon Town, where you have always dreamed of becoming a Pokétmon Trainer.")
    print("You get a call from Professor Clark, who tells you to come to his lab.")

    # First decision: go to the lab or not
    choice = input("\n\033[1;97mDo you go to the lab? (yes/no): \033[0m").lower()
    while choice not in ["yes", "no"]:
        print("Invalid choice, Please enter 'yes' or 'no'")
        choice = input("\n\033[1;97mDo you go to the lab? (yes/no): \033[0m").lower()
    if choice == "yes":
        print("\033[92mYou chose YES.\033[0m") 
        print("\nYou head to Professor Clark's lab with excitement!.")
    elif choice == "no":
        print("\033[91mYou chose NO.\033[0m")   
        print("You decide to stay home and play video games instead. Maybe another time!")
        while True:
            again = input("\n\033[1;91mDo you want to play again? (yes/no): \033[0m").lower()
            if again not in ["yes", "y"]:
                print("\033[93mThanks for playing! Goodbye!\033[0m")
                exit()
                break
            game()

    # Arriving at the lab and being told about limited choices
    print("But you arrive at Professor's lab a bit late. So there aren't many Pokétmons to choose from.")
    print("So you are a bit sad, but Professor Clark assures you that there are still some great Pokétmons left for you to choose from.")

    # Second decision: Choose a Pokétmon or not
    choose = input("\n\033[1;97mHe asks if you are you ready to choose your first Pokétmon? (yes/no): \033[0m").lower()
    while choose not in ["yes", "no"]:
        print("Invalid choice, Please enter 'yes' or 'no'")
        choose = input("\n\033[1;97mHe asks if you are you ready to choose your first Pokétmon? (yes/no): \033[0m").lower()
    if choose == "yes":
        print("\033[92mYou chose YES.\033[0m") 
        print("Professor Clark shows you the remaining Pokétmons available for you to choose from.\n")
    elif choose == "no":
        print("\033[91mYou chose NO.\033[0m")
        print("You decide to leave the lab and go home. Maybe you'll come back later.")
        while True:
            again = input("\n\033[1;91mDo you want to play again? (yes/no): \033[0m").lower()
            if again not in ["yes", "y"]:
                print("\033[93mThanks for playing! Goodbye!\033[0m")
                exit()
                break
            game()

    # Show available Pokétmon choices
    print("Here are the available Pokétmons, choose them wisely, as each Pokétmons has its strengths and weaknesses!")
    print("\033[93ma) Nimbolt:   stamina: 50 | hp: 210 | attack: 22 |\033[0m")
    print("\033[94mb) Hydrozoa:  stamina: 50 | hp: 220 | attack: 25 |\033[0m")
    print("\033[92mc) Ivyrex:    stamina: 60 | hp: 230 | attack: 23 |\033[0m")
    print("\033[95md) Hollowby:  stamina: 50 | hp: 205 | attack: 25 |\033[0m")

    # Player chooses their Pokétmon
    choose_poketmon = input("\n\033[1;97mPlease choose your Pokétmon (Enter: a,b,c,d): \033[0m").lower()
    while choose_poketmon not in ["a", "b", "c", "d"]:
            print("Invalid choice! Please choose a valid Pokétmon.")
            choose_poketmon = input("\n\033[1;97mPlease choose your Pokétmon (Enter: a,b,c,d): \033[0m").lower()

    # Assigned Pokétmon stats based on choice
    if choose_poketmon == "a":
            print("\033[93mThat's a great choice, Nimbolts are very friendly!\033[0m") 
            player_poketmon = {"name": "Nimbolt", "stamina": 50, "hp": 210, "attack": 22}
    elif choose_poketmon == "b":
            print("\033[94mSolid choice! Hydrozoa is always cool under pressure!\033[0m")
            player_poketmon = {"name": "Hydrozoa", "stamina": 50, "hp": 220, "attack": 25}
    elif choose_poketmon == "c":
            print("\033[92mIvyrex is a Strong choice!\033[0m")
            player_poketmon = {"name": "Ivyrex", "stamina": 60, "hp": 230, "attack": 23}
    elif choose_poketmon == "d":
            print("\033[95mHmm Hollowby, scary choice!\033[0m")
            player_poketmon = {"name": "Hollowby", "stamina": 50, "hp": 205, "attack": 25}
    print("")

    # Confirm player's Pokémon and start adventure
    print(f"Trainer {trainer_name} has chosen {player_poketmon['name']} which has {player_poketmon['stamina']} stamina and {player_poketmon['hp']} hp.")
    print("Congratulations on choosing your first Pokétmon!")
    print("")
    print("You head out of the lab with your new Poketmon and enter the Creek Forest, where you start your first adventure.")
    print("You are offered two choices now, either go to the Creek Forest for an exciting adventure or go back home with your new Pokétmon.")

    # Third decision: choose between forest or home
    choose = input("\n\033[1;97mEnter 'f' for Forest or 'h' for Home: \033[0m").lower()
    while choose not in ["f", "h"]:
            print("Invalid choice, Please enter 'f' for forest or 'h' for home")
            choose = input("\n\033[1;97mEnter 'f' for forest or 'h' for home: \033[0m").lower()
    if choose == "f":
        print("\033[92mYou chose Forest.\033[0m")     
        print("You are now in the Creek Forest, the most bizzare forest which is filled with a lot of wild and rare Pokétmons.")
        print("You head deep into the forest where you encounter a Pokétmon!\n")
    elif choose == "h":
        print("\033[91mYou chose Home.\033[0m")
        print("You decide to go back home with your new Pokétmon. You play with it and train for a while.")
        print("Not ready for an adventure yet. Maybe next time")
        while True:
             again = input("\n\033[1;91mDo you want to play again? (yes/no): \033[0m").lower()
             if again not in ["yes", "y"]:
                 print("\033[93mThanks for playing! Goodbye!\033[0m")
                 exit()
                 break
             game()
            

    # List of random wild opponent Pokétmon
    opponents = [
            {"name": "Pigot", "stamina": 50, "hp": 160, "attack": 16},
            {"name": "Pyroot", "stamina": 50, "hp": 180, "attack": 18},
            {"name": "Mewloo", "stamina": 50, "hp": 220, "attack": 20},
            {"name": "Moonpuffs", "stamina": 50, "hp": 140, "attack": 14},
            {"name": "Roadent", "stamina": 40, "hp": 230, "attack": 30},
            {"name": "Rocker", "stamina": 50, "hp": 200, "attack": 20},
            {"name": "Fluffin", "stamina": 50, "hp": 190, "attack": 19},
            {"name": "Buzzy", "stamina": 50, "hp": 170, "attack": 17},
            {"name": "Penop", "stamina": 50, "hp": 160, "attack": 21},
            {"name": "Froggit", "stamina": 50, "hp": 180, "attack": 18},
            {"name": "Sparky", "stamina": 50, "hp": 200, "attack": 20},
            {"name": "Flameo", "stamina": 50, "hp": 200, "attack": 22},
            {"name": "Leafy", "stamina": 50, "hp": 200, "attack": 23},
            {"name": "Cigron", "stamina": 100, "hp": 800, "attack": 100}
    ]

    # Randomly spawns an opponent
    opponent = random.choice(opponents)
    print("It's a wild {} it has {} hp.".format(opponent["name"], opponent["hp"]))
    print("You call in your Pokétmon {} to battle against the wild {}!\n".format(player_poketmon["name"], opponent["name"]))
    
    # Instructions before battle begins
    # Optional Battle Instructions
    print("\033[96mBefore the battle begins, would you like to view instructions?\033[0m")
    show_instructions = input("\033[1;97mEnter 'yes' to view instructions or 'no' to skip: \033[0m").lower()

    while show_instructions not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        show_instructions = input("\033[1;97mEnter 'yes' to view instructions or 'no' to skip: \033[0m").lower()

    if show_instructions == "yes":
        print("\n\033[94m--- Battle Instructions ---\033[0m")
        print("🔹 Space [space] = Normal Attack: Deals damage and uses 10 stamina.")
        print("🔹 X = Ultimate Move: Double damage, costs 50 stamina (requires full stamina).")
        print("🔹 R = Recharge: Restore 20 stamina and 10 HP. You can recharge up to 3 times per battle.")
        print("🔹 L = Run: Leave the battle and avoid the encounter.")
        print("Your Pokétmon and the wild Pokétmon take turns. This is a turn based strategy game!")
        print("\033[90m---------------------------\033[0m\n")
    else:
        print("\n\033[96mStarting battle!\033[0m\n")

    recharge_count = 0
    max_recharges = 3  # Maximum number of recharges allowed in a battle   
    # Battle loop: player and opponent take turns attacking, using stamina
    while player_poketmon["hp"] > 0 and opponent["hp"] > 0:
        print("\033[1;97mWhat do you want to do?\033[0m")
        print("\033[1;94mChoose action: [space] = Attack | X = Ultimate | R = Recharge | L = Run\033[0m")
        action = msvcrt.getwch().lower()
        player_acted = False
        if action == ' ':
            # Check if player has stamina
            if player_poketmon["stamina"] > 0:
                opponent["hp"] -= player_poketmon["attack"]
                player_poketmon["stamina"] -= 10  # Use stamina per attack
                print(f"You attacked {opponent['name']}! Its HP is now {opponent['hp']}. Your stamina is now {player_poketmon['stamina']}.")
                player_acted = True
                if opponent["hp"] <= 0:
                    print("\033[1;92mYou won the battle!🎉\033[0m")
                    break                    
            else:
                print("You're out of stamina! You must recharge this turn.")
                player_poketmon["stamina"] += 20  # Recharge stamina
                print(f"\033[93m{player_poketmon['name']} is recharging... Stamina is now {player_poketmon['stamina']}.\033[0m")
                # Skip attack this turn
                player_acted = True

        elif action == 'x':
            # Ultimate move, requires full stamina
            if player_poketmon["stamina"] >= 50:
                opponent["hp"] -= player_poketmon["attack"] * 2 # Ultimate move does 2x damage
                player_poketmon["stamina"] -= 50
                print(f"\033[1;93m{player_poketmon['name']} unleashed its ultimate move on {opponent['name']}! Its HP is now {opponent['hp']}.\033[0m\n")
                player_acted = True
                if opponent["hp"] <= 0:
                    print("\033[1;92mYou won the battle!🎉\033[0m")
                    break
            else:
                print(f"\033[91mNot enough stamina for ultimate move! You need at least 50 stamina.\033[0m\n")
                player_acted = True 

        elif action == 'r':
            if recharge_count < max_recharges:
                player_poketmon["stamina"] += 20
                player_poketmon["hp"] += 10
                recharge_count += 1
                print(f"\033[96m{player_poketmon['name']} used recharge! Stamina: {player_poketmon['stamina']}, HP: {player_poketmon['hp']}.\033[0m")
                print(f"\033[90mRecharges used: {recharge_count}/{max_recharges}\033[0m\n")
                player_acted = True
            else:
                print("\033[91mYou're out of recharges for this battle!\033[0m\n")              

        elif action == 'l':
            print("You ran away safely.")
            break
        else:
            print("Please choose a valid action.\n")
            continue  # Skip opponent's turn if invalid input

        # Opponent's turn (only if player acted and opponent is still alive)
        if player_acted and opponent["hp"] > 0:
            if opponent["stamina"] >= 50 and random.random() < 0.5: # 50% chance to use ultimate move
                player_poketmon["hp"] -= opponent["attack"] * 2
                opponent["stamina"] -= 50
                print(f"\033[1;95m{opponent['name']} unleashed its ultimate move on {player_poketmon['name']}! Your HP is now {player_poketmon['hp']}.\033[0m\n")
                if player_poketmon["hp"] <= 0:
                    print("\033[38;5;52mYou fainted.. better luck next time!💫\033[0m")
                    break
            elif opponent["stamina"] > 0:
                player_poketmon["hp"] -= opponent["attack"]
                opponent["stamina"] -= 10
                print(f"{opponent['name']} attacked back! Your HP is now {player_poketmon['hp']}. {opponent['name']}'s stamina is now {opponent['stamina']}.\n")
                if player_poketmon["hp"] <= 0:
                    print("\033[38;5;52mYou fainted.. better luck next time!💫\033[0m")
                    break
            else:
                print(f"{opponent['name']} is out of stamina and must recharge!")
                opponent["stamina"] += 20
                opponent["hp"] += 10 
                print(f"\033[96m{opponent['name']} is using recharge! Stamina: {opponent['stamina']}, HP: {opponent['hp']}\033[0m\n")

    print("")
    
    # End of battle: print outcome based on who fainted or if player ran
    if opponent["hp"] <= 0:
            print(f"The wild {opponent['name']} fainted. {player_poketmon['name']} held its ground like a champ.")
            print(f"You give your {player_poketmon['name']} a pat on its head, and capture the wild {opponent['name']}.")
            print("Then you head back home with your new Pokétmon, beacuse it was getting dark.")
            print("That's it for now.")
            print("\033[92mGAME OVER\033[0m")
            while True:
             again = input("\n\033[1;91mDo you want to play again? (yes/no): \033[0m").lower()
             if again not in ["yes", "y"]:
                 print("\033[93mThanks for playing! Goodbye!\033[0m")
                 exit()
                 break
             game()

    elif player_poketmon["hp"] <= 0:
            print(f"{player_poketmon['name']} hits the ground. The wild {opponent['name']} disappears into the trees.")
            print("You recall your Pokétmon and go to the health centre to recover its hp and stamina.")
            
            print("You win some, lose some.")
            print("\033[91mGAME OVER\033[0m")
            while True:
             again = input("\n\033[1;91mDo you want to play again? (yes/no): \033[0m").lower()
             if again not in ["yes", "y"]:
                 print("\033[93mThanks for playing! Goodbye!\033[0m")
                 exit()
                 break
             game()

    else: 
            print("You dip out of the place and leave the wild Pokétmon behind.")
            print("Not in the mood today to fight a wild Pokétmon.")
            print("You head back home because it was getting dark.")
            print("Maybe next time.")
            print("\033[91mGAME OVER\033[0m")
            while True:
             again = input("\n\033[1;91mDo you want to play again? (yes/no): \033[0m").lower()
             if again not in ["yes", "y"]:
                 print("\033[93mThanks for playing! Goodbye!\033[0m")
                 exit()
                 break
             game()
game()

# End of the game function