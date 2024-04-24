import random
target_number = random.randint(1, 9)
guess = 0
while guess != target_number:
    guess = int(input("Guess a number between 1 and 9: "))
print("Good guess")
