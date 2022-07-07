# sandbox version - play to check on viability of loop

# set balance for testing purposes
balance = 5

rounds_played = 0
to_play = ""
# my code is slightly different to the author
# you could trial the differences and see what happens.
while to_play != "xxx" or to_play == "":
    rounds_played +=1 # increment the rounds played
    balance -= 1 # decrement the balance by $1
    to_play = input("Press enter to play or xxx to quit: ").lower() # ask for next round
    if to_play == "xxx": # break out if player quits
        break
    # format the print statment for currency
    print("***** Round {} ***** ".format(rounds_played))
    print()
    print("Your balance is ${:.2f}".format(balance))
    print()

    if rounds_played >= 5 or balance <= 0:
        # break out of loop if balance is at 0 OR if 5 rounds been played
        if balance == 0:
            print("Sorry, you have run out of money")
        elif rounds_played == 5:
            print("Sorry, you have played all 5 rounds")
        to_play = "xxx"




print("play ends")

