"""
base component for the game Lucky Unicorn
V0 - skeleton setup
v1 - instructions set up, yes no component and instructions component added

author- Whaea Suzanne
CC WSA 2022

"""

# import libraries below this line **************************

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

show_instructions_q = "Have you played this game before? "
response = yes_no(show_instructions_q)
if response == "yes":
    print("program continues")
else:
    instructions()
