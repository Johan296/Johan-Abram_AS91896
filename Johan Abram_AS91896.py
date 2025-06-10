print("""
  __  __           _         ____        _      
 |  \/  |         (_)       / __ \      (_)     
 | \  / |_   _ ___ _  ___  | |  | |_   _ _ ____ 
 | |\/| | | | / __| |/ __| | |  | | | | | |_  / 
 | |  | | |_| \__ \ | (__  | |__| | |_| | |/ /  
 |_|  |_|\__,_|___/_|\___|  \___\_\\__,_|_/___| 
                                                                                               
""")
# This is a simple music quiz coding that asks the user five questions about music.
score = 0
print("Welcome to the Music Quiz!")
print("This is a quiz about famous music artists and their songs.")

# Question 1 
print("What is the name of the artist who got featured in the song 'Like that'?")
print("a) Drake")
print("b) Kendrick Lamar")
print("c) Travis Scott")
print("d) J. Cole")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "b":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is b) Kendrick Lamar")
    print("-------------------------")

# Question 2
print("Which of the following is not an album of the artist 'Kendrick Lamar'?")
print("a) Scorpion")
print("b) GNX")
print("c) DAMN.")
print("d) To Pimp a Butterfly")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "a":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is a) Scorpion")
    print("-------------------------")

# Question 3
print("What is the real name of the artist 'Eminem'?")
print("a) Mathew Marshall")
print("b) Mathew Mather")
print("c) Marshall Mathew")
print("d) Marshall Mather")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "d":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is d) Marshall Mather")
    print("-------------------------")

# Question 4
print("Who found the XO record label?")
print("a) Travis Scott")
print("b) Dr. Dre")
print("c) The Weeknd")
print("d) Drake")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "c":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is c) The Weeknd")
    print("-------------------------")

# Question 5
print("How many songs does the Weeknd have that are over 1 billion streams?")
print("a) 5")
print("b) 27")
print("c) 19")
print("d) 10")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "b":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is b) 27")
    print("-------------------------")

# Question 6
print("Which rapper is known for the album 'I AM MUSIC'?")
print("a) Playboi Carti")
print("b) Tyler the creator")
print("c) Lil wayne")
print("d) Kid cudi")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "a":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is a) Playboi Carti")
    print("-------------------------")

# Question 7
print("In which animated series did D4vd's song 'Feel it' got played?")
print("a) Devil may cry")
print("b) My hero academia")
print("c) Tokyo Ghoul")
print("d) Invincible")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "d":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is d) Invincible")
    print("-------------------------")
   
# Question 8
print("In which D4vd's album the song 'Feel it' got played?")
print("a) Weathered")
print("b) Willows in the wind")
print("c) Withered")
print("d) Witch Craft")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "c":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is c) Withered")
    print("-------------------------")

# Question 9
print("What is Kali Uchis' most popular song?")
print("a) Moon Light")
print("b) See you again")
print("c) Telepatia")
print("d) I wish you roses")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "c":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is c) Telepatia")
    print("-------------------------")

# Question 10
print("What is the name of the Artist who got featured in the song 'See you again' by Tyler the Creator?")
print("a) Kali Uchis")
print("b) Taylot Swift")
print("c) Don Toliver")
print("d) Charlie Puth")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "a":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect, the correct answer is a) Kali Uchis")
    print("-------------------------")

# Final score
print("Quiz completed!")
print("You have finished the Music Quiz")
print("Score:", score,"out of 10")
