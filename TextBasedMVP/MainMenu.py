import time

print("Welcome to Chain Reaction!")
print("This is a game for 2-8 players, where the objective is to be the last player standing.")
print("Find the rules and tutorial for the game at: \
https://brilliant.org/wiki/chain-reaction-game/ \n")

print("We will now ask you basic details required to start the game.\n")
time.sleep(2)

invalidInput = True

while invalidInput:
    try:
        numPlayers = int(input("Enter the number of players:"))

    except:
        print("Please enter an integer!")

    else:

        if numPlayers > 8:

            print("No more than 8 players are allowed!")

        elif numPlayers < 2:

            print("You need at least 2 Players to play the game!")

        else:

            invalidInput = False

    print()
    time.sleep(1)

