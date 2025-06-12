import random

print("""
 ______     _                                _____                       
| ___ \   | |                              |  __ \                      
| |_/ /__ | | _____ _ __ ___   ___  _ __   | |  \/ __ _ _ __ ___   ___  
|  __/ _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \  | | __ / _` | '_ ` _ \ / _ \ 
| | | (_) |   <  __/ | | | | | (_) | | | | | |_\ \ (_| | | | | | |  __/ 
\_|  \___/|_|\_\___|_| |_| |_|\___/|_| |_|  \____/\__,_|_| |_| |_|\___| 
""")

print("Welcome to the Pokémon Game!")
print("In this game, you will choose a Pokémon and battle against another Pokémon.")
trainer_name = input(" Please enter your trainer name: ")
print(f"Welcome, {trainer_name}! Let's start your Pokémon adventure!")

pokemon_list = {
    "Charizard": {"type":"Fire","hp": 310,"attack": 50},
    "Blastoise": {"type":"Water","hp": 320,"attack": 52},
    "Venusaur": {"type":"Grass","hp": 350,"attack": 45},
    "Raichu": {"type":"Electric","hp": 200,"attack": 60}
}

type_chart = {
    "Fire": "Grass",
    "Water": "Fire",
    "Grass": "Water",
    "Electric": "Water",
}

def choose_pokemon():
    print("Choose your Pokémon:")
    for index, name in enumerate(pokemon_list.keys(), 1):
        print(f"{index}. {name}")
    while True:
        try:
            choice = int(input("Enter the number of your Pokemon: "))
            if 1 <= choice <= len(pokemon_list):
                return list(pokemon_list.keys())[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")



print("Game over.")