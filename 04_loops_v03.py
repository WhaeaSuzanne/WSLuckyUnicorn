# sandbox version - play to check on viability of loop
import random

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# set balance for testing purposes
balance = 5
rounds_played = 0
to_play = ""
# my code is slightly different to the author
# you could trial the differences and see what happens.

while to_play != "xxx" or to_play == "":
    rounds_played +=1 # increment the rounds played
    to_play = input("Press enter to play or xxx to quit: ").lower() # ask for next round
    if to_play == "xxx": # break out if player quits
        break
    # format the print statment for currency
    print("***** Round {} ***** ".format(rounds_played))
    print()
    print("Your starting balance is ${:.2f}".format(balance))
    print()
    chosen_num = random.randint(1,100)
    # x += 1
    # print(x, chosen, end='\t')

    # adjust the balance
    if 1 <= chosen_num <= 5 :
        # this is the percentage chance of getting a unicorn
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36 :
        chosen = "donkey"
        balance -= 1
    else: # all the numbers between 1 and 36 have been checked
        if chosen_num % 2 == 0:
        # modulo % 2 means that the number is divided and
        # the remainder is applied. The remainder should be
        # an even number to be a horse
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your final balance is ${:.2f}".format(chosen, balance))
    print()
    if rounds_played >= 5 or balance <= 0:
        # break out of loop if balance is at 0 OR if 5 rounds been played
        if balance <= 0:
            print("Sorry, you have run out of money")
        elif rounds_played == 5:
            print("Sorry, you have played all 5 rounds")
        to_play = "xxx"

print("Thanks for Playing")

