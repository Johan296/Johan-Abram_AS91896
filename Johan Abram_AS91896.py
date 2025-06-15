# This is a simple Pokémon game where the player chooses a Pokémon and battles against another Pokémon.

print(""" 
  ____       _        _                         
 |  _ \ ___ | | _____| |_ _ __ ___   ___  _ __  
 | |_) / _ \| |/ / _ \ __| '_ ` _ \ / _ \| '_ \ 
 |  __/ (_) |   <  __/ |_| | | | | | (_) | | | |
 |_|   \___/|_|\_\___|\__|_| |_| |_|\___/|_| |_|                                             
""")

print("Welcome to your Pokétmon Adventure!")
trainer_name = input("First of all, Please enter your trainer name: ")
print(f"\nWelcome, trainer {trainer_name}! Let's start your Pokétmon adventure!")
print("You wake up in Paimon Town, where you have always dreamed of becoming a Pokétmon Trainer.")
print("You get a call from Professor Clark, who tells you to come to his lab.")

choice = input("Do you go to the lab? (yes/no): ").lower()
if choice == "yes":
        print("\nYou head to Professor Clark's lab with excitement!.")
elif choice == "no":
        print("You decide to stay home and play video games instead. Maybe another time!")
        exit()

print("You arrive at Professor Clark's lab, where you see him waiting for you along with his nephew Barley, who happens to be your rival.")
print("Professor greets you and you greet him back and then he tells you that Barley has already chosen his first Pokétmon which is a Flametail,"
            " the one you wanted to choose. Barley knows that you wanted it so he smirks and says, "
            f"'Too bad {trainer_name}, first come first serve!'")
print("You feel a bit sad, but Professor Clark assures you that there are other great Pokétmons available for you to choose from.")

choose = input("\nHe asks if you are you ready to choose your first Pokétmon? (yes/no): ").lower()
if choose == "yes":
        print("Professor Clark shows you the remaining Pokétmons available for you to choose from.\n")
elif choose == "no":
        print("You decide to leave the lab and go home. Maybe you'll come back later.")
        exit()

print("Here are the available Pokétmons, choose them wisely, as each type has its strengths and weaknesses!")
print("a) Nimbolt:   Type: Electric, hp: 190, attack: 20 | Strong against: Water   | Weak against: Psychic")
print("b) Hydrozoa:  Type: Water,    hp: 220, attack: 20 | Strong against: Fire    | Weak against: Electric")
print("c) Ivyrex:    Type: Grass,    hp: 230, attack: 20 | Strong against: Water   | Weak against: Fire")
print("d) Hollowby:  Type: Dark,     hp: 205, attack: 20 | Strong against: Psychic | Weak against: Electric")

# The player's choice of Pokétmon
choose_poketmon = input("\nPlease choose your Pokétmon (Enter: a,b,c,d): ").lower()
while choose_poketmon not in ["a", "b", "c", "d"]:
        print("Invalid choice! Please choose a valid Pokétmon.")
        choose_poketmon = input("Please choose your Pokétmon (Enter: a,b,c,d): ").lower()

if choose_poketmon == "a":
        print("That's a great choice, Nimbolts are very friendly!")
        player_poketmon = {"name": "Nimbolt", "type": "Electric", "hp": 190, "attack": 20}
elif choose_poketmon == "b":
        print("Solid choice! Hydrozoa is always cool under pressure!")
        player_poketmon = {"name": "Hydrozoa", "type": "Water", "hp": 220, "attack": 20}
elif choose_poketmon == "c":
        print("Strong choice!")
        player_poketmon = {"name": "Ivyrex", "type": "Grass", "hp": 230, "attack": 20}
elif choose_poketmon == "d":
        print("Hmm Hollowby, scary choice!")
        player_poketmon = {"name": "Hollowby", "type": "Dark", "hp": 205, "attack": 20}
print("")

print(f"Trainer {trainer_name} has chosen {player_poketmon['name']} which is a {player_poketmon['type']} type and has {player_poketmon['hp']} hp.")
print("You are now ready to start your adventure with your new Pokétmon!")
print("")
print("Professor Clark gives you the Pokétmon Ball and tells you to take good care of your new Pokétmon.")
print("You thank him and start packing your bag with some essentials and wish farewell to Professor Clark and Barley.")
# The player will now embark on his journey to catch more Pokémon


# Opponent Pokémon
opponent = {"name": "Pigot", "type": "Flying", "hp": 150, "attack": 15}
print("A wild {} appeared! It has {} hp.".format(opponent["name"], opponent["hp"]))

# Begin battle loop
while player_poketmon["hp"] > 0 and opponent["hp"] > 0:
    print("What do you want to do? (attack/run)")
    action = input("> ").lower()
    
    if action == "attack":
        opponent["hp"] -= player_poketmon["attack"]
        print(f"You attacked {opponent['name']}! Its HP is now {opponent['hp']}.")
        if opponent["hp"] <= 0:
            print("You won the battle!🎉")
            break
        player_poketmon["hp"] -= opponent["attack"]
        print(f"{opponent['name']} attacked back! Your HP is now {player_poketmon['hp']}.")
        if player_poketmon["hp"] <= 0:
            print("You fainted... better luck next time! 💫")
            break
    elif action == "run":
        print("You ran away safely.")
        break
    else:
        print("Please choose a valid action.")