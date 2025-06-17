import random
import msvcrt

# Prints welcome message
print(""" 
  ____       _        _                         
 |  _ \ ___ | | _____| |_ _ __ ___   ___  _ __  
 | |_) / _ \| |/ / _ \ __| '_ ` _ \ / _ \| '_ \ 
 |  __/ (_) |   <  __/ |_| | | | | | (_) | | | |
 |_|   \___/|_|\_\___|\__|_| |_| |_|\___/|_| |_|                                             
""")

# Introduction and trainer name input
print("Welcome to Pokétmon Adventure!")
trainer_name = input("To start please enter your trainer name: ")
print(f"\nWelcome, trainer {trainer_name}! Let's start your Pokétmon adventure!")
print("You wake up in Paimon Town, where you have always dreamed of becoming a Pokétmon Trainer.")
print("You get a call from Professor Clark, who tells you to come to his lab.")

# First decision: go to the lab or not
choice = input("Do you go to the lab? (yes/no): ").lower()
if choice == "yes":
        print("\nYou head to Professor Clark's lab with excitement!.")
elif choice == "no":
        print("You decide to stay home and play video games instead. Maybe another time!")
        exit()

# Arriving at the lab and being told about limited choices
print("But you arrive at Professor's lab a bit late. So there aren't many Pokétmons to choose from.")
print("So you are a bit sad, but Professor Clark assures you that there are still some great Pokétmons left for you to choose from.")

# Second decision: Choose a Pokétmon or not
choose = input("\nHe asks if you are you ready to choose your first Pokétmon? (yes/no): ").lower()
if choose == "yes":
        print("Professor Clark shows you the remaining Pokétmons available for you to choose from.\n")
elif choose == "no":
        print("You decide to leave the lab and go home. Maybe you'll come back later.")
        exit()

# Show available Pokétmon choices
print("Here are the available Pokétmons, choose them wisely, as each type has its strengths and weaknesses!")
print("a) Nimbolt:   stamina: 150 | hp: 210 | attack: 22 |")
print("b) Hydrozoa:  stamina: 150 | hp: 220 | attack: 22 |")
print("c) Ivyrex:    stamina: 160 | hp: 230 | attack: 21 |")
print("d) Hollowby:  stamina: 150 | hp: 205 | attack: 23 |")

# Player chooses their Pokétmon
choose_poketmon = input("\nPlease choose your Pokétmon (Enter: a,b,c,d): ").lower()
while choose_poketmon not in ["a", "b", "c", "d"]:
        print("Invalid choice! Please choose a valid Pokétmon.")
        choose_poketmon = input("Please choose your Pokétmon (Enter: a,b,c,d): ").lower()

# Assigned Pokétmon stats based on choice
if choose_poketmon == "a":
        print("That's a great choice, Nimbolts are very friendly!")
        player_poketmon = {"name": "Nimbolt", "stamina": 150, "hp": 210, "attack": 22}
elif choose_poketmon == "b":
        print("Solid choice! Hydrozoa is always cool under pressure!")
        player_poketmon = {"name": "Hydrozoa", "stamina": 150, "hp": 220, "attack": 22}
elif choose_poketmon == "c":
        print("Strong choice!")
        player_poketmon = {"name": "Ivyrex", "stamina": 160, "hp": 230, "attack": 21}
elif choose_poketmon == "d":
        print("Hmm Hollowby, scary choice!")
        player_poketmon = {"name": "Hollowby", "stamina": 150, "hp": 205, "attack": 23}
print("")

# Confirm player's Pokémon and start adventure
print(f"Trainer {trainer_name} has chosen {player_poketmon['name']} which has {player_poketmon['stamina']} stamina and {player_poketmon['hp']} hp.")
print("You are now ready to start the battle with your new Pokétmon!")
print("")
print("You head out of the lab with your new Poketmon, and you enter the Creek Forest")
print("You are now in the Creek Forest, the most bizzare forest which is filled with a lot of wild and rare Pokétmons.")
print("You head deep into the forest where you encounter a Pokétmon!\n")

# Random wild opponent Pokétmon
opponents = [
        {"name": "Pigot", "stamina": 100, "hp": 160, "attack": 16},
        {"name": "Pyroot", "stamina": 120, "hp": 180, "attack": 18},
        {"name": "Mewloo", "stamina": 150, "hp": 220, "attack": 20},
        {"name": "Moonpuffs", "stamina": 110, "hp": 140, "attack": 14},
        {"name": "Roadent", "stamina": 140, "hp": 250, "attack": 18},
        {"name": "Rocker", "stamina": 125, "hp": 200, "attack": 20},
        {"name": "Fluffin", "stamina": 115, "hp": 190, "attack": 19},
        {"name": "Buzzy", "stamina": 105, "hp": 170, "attack": 17}
]

# Randomly spawns an opponent
opponent = random.choice(opponents)
print("It's a wild {} It has {} hp.".format(opponent["name"], opponent["hp"]))
print("You call in your Pokétmon {} to battle against the wild {}!".format(player_poketmon["name"], opponent["name"]))

# Battle loop: player and opponent take turns attacking
print("Press [space] to attack, or type 'run' to run away.")
while player_poketmon["hp"] > 0 and opponent["hp"] > 0:
        print("What do you want to do? (attack/run)")
        print("Press [space] to attack, or type 'run' and press [Enter] to run away.")
        action = msvcrt.getwch()
        if action == ' ':
                # Player attacks opponent
                opponent["hp"] -= player_poketmon["attack"]
                print(f"You attacked {opponent['name']}! Its HP is now {opponent['hp']}.")
                if opponent["hp"] <= 0:
                        print("You won the battle!🎉")
                        break
                # Opponent attacks back
                player_poketmon["hp"] -= opponent["attack"]
                print(f"{opponent['name']} attacked back! Your HP is now {player_poketmon['hp']}.\n")
                if player_poketmon["hp"] <= 0:
                        print("You fainted... better luck next time! 💫")
                        break
        elif action == "run":
                # Player runs away
                print("You ran away safely.")
                break
        else:
                print("Please choose a valid action.")

print("")
# End of battle: print outcome based on who fainted or if player ran
if opponent["hp"] <= 0:
        print(f"The wild {opponent['name']} fainted. {player_poketmon['name']} held its ground like a champ.")
        print("You give it a pat on it's head. No big speeches—just respect.")
        print("You turn around, brush the dirt off your Poketmon, and start heading back through the forest.")
        print("That's it for now.")
        print("GAME OVER")

elif player_poketmon["hp"] <= 0:
        print(f"{player_poketmon['name']} hits the ground. The wild {opponent['name']} disappears into the trees.")
        print("You recall your Pokétmon silently and walk out of the forest, not feeling defeated, just... done.")
        print("You win some, lose some.")
        print("GAME OVER")

else:
        print("You dip out of the battle and leave the forest behind.")
        print("Not in the mood today. Fair enough.")
        print("Maybe next time.")
        print("GAME OVER")