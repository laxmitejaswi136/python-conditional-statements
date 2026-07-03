import random

number = random.randint(1, 100)

guess = input("Guess (Odd/Even): ").lower()

if number % 2 == 0:
    actual = "even"
else:
    actual = "odd"

print("Random Number:", number)

if guess == actual:
    print("Correct Guess!")
else:
    print("Wrong Guess!")