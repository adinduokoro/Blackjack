import random
import sys


def getbet(max_money):
    return max_money


def main():
    print('''
    Rules:
        Try to get close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it, to take another card.
        (S)tand to stop taking card.
        On your first play, you can double down to increase your bet but 
        must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.\n''')

    money = 500
    while True:  # Main Game loop
        if money < 0:  # Check to see if player ran out of money
            print("You ran out of fake money!\nGoodbye =]")
            sys.exit()

        # Get the players bet
        print("Money: " + str(money))
        bet = getbet(money)


if __name__ == "__main__":
    main()
