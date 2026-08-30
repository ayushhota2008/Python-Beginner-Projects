# Number Gussing Game
import random
bot = random.randint(1,100)
print("WELCOME TO THE NUMBER GUESSING GAME")
print("Bot choosing its number........")
print("Bot choosed its number")

tries = 0
while True:
    tries += 1
    player = int(input("Your turn to choose number from 1-100:"))

    if player == bot:
        print("CONGRATULATIONS YOU WON THE GAME")
        print(f"Your total tries={tries}")
        break

    elif player > bot:
        print("Wrong guess go little lower!")

    elif player < bot:
        print("Wrong guess go little higher!")