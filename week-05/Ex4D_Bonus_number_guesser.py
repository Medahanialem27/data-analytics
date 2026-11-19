game_limits = (1, 10)
number_pool = list(range(game_limits[0], game_limits[1] +11))

import time
target_index = time.time_ns() % len(number_pool)
target_number = number_pool[target_index]

guesses = []
while True:
        try:
                guess= int(input("Enter your guess: "))
                break
        except ValueError:
            print("Please enter a whole number.")
guesses.append(guess)
guess_count = 1

while guess != target_number:
            if guess < target_number:
                    print("Higher")
            else:
                    print("Lower")

            guess = int(input("Guess again: "))
            guesses.append(guess)
            guess_count = guess_count + 1

print("Correct!")
print("Your guesses were:", guesses)
print("Number of guesses:", guess_count)
if guess_count < 5:
    print("Awesome! you guessed it in fewer than 5 tries!")
    
while True:
        try:
                guess= int(input("Enter your guess: "))
                break
        except ValueError:
            print("Please enter a whole number.")

    

