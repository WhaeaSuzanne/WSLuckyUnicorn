"""
base component for the game Lucky Unicorn
V0 - skeleton setup
v1 - instructions set up, yes no component and instructions component added
v2 - token generator and payout calculator added
author- Whaea Suzanne
CC WSA 2022

"""

# import libraries below this line **************************
import random

# all functions below this line **************************


def instructions():
    # rules will be added as they are required

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


# main routine below this line **************************
STARTING_BALANCE = 100

balance = STARTING_BALANCE

show_instructions_q = "Have you played this game before? "
response = yes_no(show_instructions_q)
if response == "yes":
    print("program continues")
else:
    instructions()

# token generator and payout calculator
for item in range(0, 20):
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
print("Starting balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
