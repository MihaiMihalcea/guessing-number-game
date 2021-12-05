import random

logo = '''
 .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .-----------------..----------------. .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |    ______    | | | _____  _____ | | |  _________   | | |    _______   | | |    _______   | | |              | | | ____  _____  | | | _____  _____ | | | ____    ____ | | |   ______     | | |  _________   | | |  _______     | |
| |  .' ___  |   | | ||_   _||_   _|| | | |_   ___  |  | | |   /  ___  |  | | |   /  ___  |  | | |              | | ||_   \|_   _| | | ||_   _||_   _|| | ||_   \  /   _|| | |  |_   _ \    | | | |_   ___  |  | | | |_   __ \    | |
| | / .'   \_|   | | |  | |    | |  | | |   | |_  \_|  | | |  |  (__ \_|  | | |  |  (__ \_|  | | |    ______    | | |  |   \ | |   | | |  | |    | |  | | |  |   \/   |  | | |    | |_) |   | | |   | |_  \_|  | | |   | |__) |   | |
| | | |    ____  | | |  | '    ' |  | | |   |  _|  _   | | |   '.___`-.   | | |   '.___`-.   | | |   |______|   | | |  | |\ \| |   | | |  | '    ' |  | | |  | |\  /| |  | | |    |  __'.   | | |   |  _|  _   | | |   |  __ /    | |
| | \ `.___]  _| | | |   \ `--' /   | | |  _| |___/ |  | | |  |`\____) |  | | |  |`\____) |  | | |              | | | _| |_\   |_  | | |   \ `--' /   | | | _| |_\/_| |_ | | |   _| |__) |  | | |  _| |___/ |  | | |  _| |  \ \_  | |
| |  `._____.'   | | |    `.__.'    | | | |_________|  | | |  |_______.'  | | |  |_______.'  | | |              | | ||_____|\____| | | |    `.__.'    | | ||_____||_____|| | |  |_______/   | | | |_________|  | | | |____| |___| | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' 
'''
print(logo)
print("Welcome to the number guessing game")
difficulty = input("Would you like to play the game on easy or hard mode?: ")
number = random.randint(1, 100)
def play():
    game_on = True
    print("I'm thinking of a game between 1 and 100")
    if difficulty == 'easy':
        guesses = 10
        while game_on:
            guess = int(input("Make a guess: "))
            if guess == number:
                print("You have guessed the number, congratulations!")
                game_on = False
            elif guess > number:
                print("You guessed too high, try again.")
                guesses -= 1
                if guesses > 0:
                    print(f"You have {guesses} tries left.")
                else:
                    print("You have ran out of guesses.")
                    print(f"The number was {number}.")
                    game_on = False
            elif guess < number:
                print("You have guessed too low, try again.")
                guesses -= 1
                if guesses > 0:
                    print(f"You have {guesses} tries left.")
                else:
                    print("You have ran out of guesses.")
                    print(f"The number was {number}.")
                    game_on = False
    elif difficulty == 'hard':
        guesses = 5
        while game_on:
            guess = int(input("Make a guess: "))
            if guess == number:
                print("You have guessed the number, congratulations!")
                game_on = False
            elif guess > number:
                print("You guessed too high, try again.")
                guesses -= 1
                if guesses > 0:
                    print(f"You have {guesses} tries left.")
                else:
                    print("You have ran out of guesses.")
                    print(f"The number was {number}.")
                    game_on = False
            elif guess < number:
                print("You have guessed too low, try again.")
                guesses -= 1
                if guesses > 0:
                    print(f"You have {guesses} tries left.")
                else:
                    print("You have ran out of guesses.")
                    print(f"The number was {number}.")
                    game_on = False

play()