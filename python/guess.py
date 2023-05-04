import random
numero=random.randint(1,7)
tries = 0
guess = 0

print("============")
print("From 1 to 7\nYou have 5 tries")
print("============")

while n5umero != guess and tries < 5:
    guess = int(input("Guess the number :  "))
    tries += 1

if numero != guess:
    print("Game over, the number was",numero)
else:
    print("You got it!")
