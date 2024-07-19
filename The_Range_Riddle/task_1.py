# Task 1: Print every other day of the week
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("Printing days of the week at even indices:")
for i in range(len(days_of_week)):
    if i % 2 == 0:
        print(days_of_week[i])

# Task 2: Simulate moods for different days
import random

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["Happy", "Sad", "Excited", "Tired", "Bored", "Anxious", "Relaxed"]

print("\nMoods for different days of the week:")
for day in days_of_week:
    mood = random.choice(moods)
    print(f"{day}: {mood}")

# Task 3: Create a countdown timer
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Set countdown time in seconds
countdown_time = 10  # For example, a 10-second countdown
print("\nStarting countdown timer:")
countdown_timer(countdown_time)
