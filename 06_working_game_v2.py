"""
base component for the game Lucky Unicorn
V0 - skeleton setup
v1 - instructions set up, yes no component and instructions component added
v2.1 - set up the game loops, token generator and balance added. Working game (basic)
author- Whaea Suzanne
renamed to 06_working_game_v1
v2 - add the decoration function, add print generate decoration to all the token generator statements

CC WSA 2022

"""

# import libraries below this line **************************
import random
# all functions below this line **************************


def instructions():
    # rules will be added as they are required
    print()
    print("************   How to play   ************")
    print()
    print("***  The rules of the game go here.  ***")
    print()
    return ""


def yes_no(question):

    """function to test user response to be yes or no and return this
        the question is a parameter, the response is edited and returned to the main
        """

    valid = "False"
    while valid:
        # ask user if they have played before
        response_u = input(question).lower()

        if response_u == "yes" or response_u == "y":
            # if they say yes, return yes
            response_u = "yes"
            return response_u

        elif response_u == "no" or response_u == "n":
            # if no, then return no
            response_u = "no"
            return response_u

        else:
            print("please enter yes or no.")


def statement_generator (statement, decoration):
    # generate decorations around the statements.
    # parameters received include the statement and the decoration to be added.
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# variables and constants below this line ***************
STARTING_BALANCE = 10

balance = STARTING_BALANCE
rounds_played = 0
to_play = ""
welcome_greeting = "Welcome to the Lucky Unicorn game."
welcome_decoration = "*"

# main routine below this line **************************

statement_generator(welcome_greeting, welcome_decoration)
print()


show_instructions_q = "Have you played this game before? "
response = yes_no(show_instructions_q)
if response == "no":
    instructions()

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
        chosen_statement = "Congratulations, you got a unicorn"
        chosen_decoration = "!"

    elif 6 <= chosen_num <= 36 :
        chosen = "donkey"
        balance -= 1
        chosen_statement = "Oops, you got a donkey - hee haw!"
        chosen_decoration = "D"
    else: # all the numbers between 1 and 36 have been checked
        if chosen_num % 2 == 0:
        # modulo % 2 means that the number is divided and
        # the remainder is applied. The remainder should be
        # an even number to be a horse
            chosen = "horse"
            chosen_statement = "You got a horse."
            chosen_decoration = "H"
        else:
            chosen = "zebra"
            chosen_statement = "You got a zebra."
            chosen_decoration = "Z"
        balance -= 0.5

    statement_generator(chosen_statement, chosen_decoration)
    print("Your final balance is ${:.2f}".format(balance))
    print()
    if rounds_played >= 5 or balance <= 0:
        # break out of loop if balance is at 0 OR if 5 rounds been played
        if balance <= 0:
            print("Sorry, you have run out of money")
        elif rounds_played == 5:
            print("Sorry, you have played all 5 rounds")
        to_play = "xxx"

print("Thanks for Playing")
