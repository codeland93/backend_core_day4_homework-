import random

# List of items
items = ["apple", "banana", "orange", "grape", "pear"]

# Randomly select an item from the list
selected_item = random.choice(items)

print("Welcome to the Random Choice Game!")
print("Guess which item was selected from the list: ", items)

while True:
    guess = input("Enter your guess: ")
    
    if guess == selected_item:
        print("Congratulations! You guessed correctly!")
        break
    else:
        print("Sorry, that's not correct. Try again!")
