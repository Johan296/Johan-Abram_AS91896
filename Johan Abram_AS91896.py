#This is a simple Pokémon game where the player chooses a Pokémon and battles against another Pokémon.

print("""
______     _                                ______                       
| ___ \   | |                              |  __ \                      
| |_/ /__ | | _____ _ __ ___   ___  _ __   | |  \/ __ _ _ __ ___   ___  
|  __/ _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \  | | __ / _` | '_ ` _ \ / _ \ 
| | | (_) |   <  __/ | | | | | (_) | | | | | |_\ \ (_| | | | | | |  __/ 
\_|  \___/|_|\_\___|_| |_| |_|\___/|_| |_|  \____/\__,_|_| |_| |_|\___| 
""")

print("Welcome to the Pokémon Game!")
print("In this game, you will choose a Pokémon and battle against another Pokémon.")
game = input("Are you ready to start your Pokémon adventure? (yes/no): ").lower()
if game == "yes":
    print("Lets get started!")
elif game == "no":
    print("No problem! You can come back anytime to play.")
    exit()
trainer_name = input("First of all, Please enter your trainer name: ")
print("Welcome, {}! Let's start your Pokémon adventure!".format(trainer_name))

print("------------------------------------")

print("Here is the list of available starter Pokémons and their type charts:")
print("This is the Type Chart,\n  Fire > Grass\n  Water > Fire\n  Electric > Water\n  Psychic > Electric\n  Ghost > Psychic")
print("------------------------------------")
print("Choose your Pokémon wisely, as each type has its strengths and weaknesses!")
print("a)Pikachu: Type: Electric, hp: 190, attack:20"),
print("b)Squitle: Type: Water, hp: 220, attack:20"),
print("c)Charmander: Type: Fire, hp: 200, attack:20"),
print("d)Bulbasaur: Type: Grass, hp: 230, attack:20")
print("e)Kadabra: Type: Psychic, hp: 215, attack:22")
print("f)Ghastly: Type: Dark, hp: 205, attack:20")

# The player's choice of Pokémon
choose_pokemon = input("Please choose your Pokémon (Enter: a,b,c,d,e,f): ").lower()
while choose_pokemon not in ["a", "b", "c", "d", "e", "f"]:
    print("Invalid choice! Please choose a valid Pokémon.")
    choose_pokemon = input("Please choose your Pokémon (Enter: a,b,c,d,e,f): ").lower()
if choose_pokemon == "a":
    print("That's a great choice, Pikachu is very friendly!")
    player_pokemon = {"name": "Pikachu", "type": "Electric", "hp": 190, "attack": 20}
elif choose_pokemon == "b":
    print("You have chosen Squirtle!")
    player_pokemon = {"name": "Squirtle", "type": "Water", "hp": 220, "attack": 20}
elif choose_pokemon == "c":
    print("You have chosen Charmander!")
    player_pokemon = {"name": "Charmander", "type": "Fire", "hp": 200, "attack": 20}
elif choose_pokemon == "d":
    print("You have chosen Bulbasaur!")
    player_pokemon = {"name": "Bulbasaur", "type": "Grass", "hp": 230, "attack": 20}
elif choose_pokemon == "e":
    print("Unique choice, no one chooses this usually!")
    player_pokemon = {"name": "Kadabra", "type": "Psychic", "hp": 215, "attack": 22}
elif choose_pokemon == "f":
    print("Hmm Ghastly, scary choice!")
    player_pokemon = {"name": "Ghastly", "type": "Dark", "hp": 205, "attack": 20}

print("------------------------------------")
print("{} has chosen {} which is a {} type and has {} hp.".format( trainer_name, player_pokemon["name"], player_pokemon["type"], player_pokemon["hp"]))
print("Now, the story begins...")
print("------------------------------------")
    