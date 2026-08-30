import random
print("*******WELCOME TO ROCK,PAPER AND SCISSOR GAME*******")
players_score = 0
bots_score = 0

while True:
    bot = random.choice(["rock","paper","scissor"])
    print("Bot has already chosen:)")
    player = input("Your turn choose rock,paper or scissor:")

    if player == bot:
        print(f"Bot chose: {bot}")
        print(f"Players score: {players_score}")
        print(f"Bots score: {bots_score}")
        print("Draw")

    elif player=="rock" and bot=="paper":
        print(f"Bot chose:{bot}")
        bots_score+=1
        print(f"Bots score:{bots_score}")
        print(f"Players score:{players_score}")
        print("Bot Wins")
    
    elif player=="paper" and bot=="rock":
        print(f"Bot chose:{bot}")
        players_score+=1
        print(f"Players score:{players_score}")
        print(f"Bots score:{bots_score}")
        print("Player Wins")
    
    elif player=="rock" and bot=="scissor":
        print(f"Bot chose:{bot}")
        players_score+=1
        print(f"Players score:{players_score}")
        print(f"Bots score:{bots_score}")
        print("Player Wins")

    elif player=="scissor" and bot=="rock":
        print(f"Bot chose:{bot}")
        bots_score+=1
        print(f"Bots score:{bots_score}")
        print(f"Players score:{players_score}")
        print("Bot wins")
    
    elif player=="scissor" and bot=="paper":
        print(f"Bot chose:{bot}")
        players_score+=1
        print(f"Players score:{players_score}")
        print(f"Bots score:{bots_score}")
        print("Player Wins")
    
    elif player=="paper" and bot=="scissor":
        print(f"Bot chose:{bot}")
        bots_score+=1
        print(f"Bots score:{bots_score}")
        print(f"Players score:{players_score}")
        print("Bot Wins")

    else:
        print("Invalid input!!!")
        break


    if players_score == 5:
        print(f"Player Wins the game by {players_score} points ")
        break
    elif bots_score == 5:
        print(f"Bot Wins the game by {bots_score} points")
        break