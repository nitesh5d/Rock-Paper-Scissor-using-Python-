import random
chance = 0
bot_points = 0
player_points = 0
while chance != 10:
    print("\n")
    print("Round", chance+1)
    words = ["rock","paper","scissor"]
    bot_input = random.choice(words)
    player_input = input("rock/paper/scissor: ").lower()
    print("Your Selection: ", player_input)
    print("Bot Selection: ",bot_input)

    if bot_input ==  player_input: print("Tie")
    elif bot_input == 'rock' and player_input == 'paper':
        print("Player Won")
        player_points+=1
    elif bot_input == 'rock' and player_input == 'scissor':
        print("Bot Won")
        bot_points+=1
    elif bot_input == 'paper' and player_input == 'rock':
        print("Bot Won")
        bot_points+=1
    elif bot_input == 'paper' and player_input == 'scissor':
        print("Player Won")
        player_points+=1
    elif bot_input == 'scissor' and player_input == 'rock':
        print("Player Won")
        player_points+=1
    elif bot_input == 'scissor' and player_input == 'paper':
        print("Bot Won")
        bot_points+=1
    else: print("Invalid Input")

    chance +=1
print('\n')
print("Bot Points-",bot_points)
print("Player Points-",player_points)
if bot_points > player_points:
    print("Bot won the match")
elif player_points > bot_points:
    print("Player won the match")
