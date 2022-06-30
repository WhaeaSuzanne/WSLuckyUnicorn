"""
function to print instructions to the screen
v1 - set up the function
v2 - add the yes no function to run the program. This will become the v1 base component
"""
# functions go below this line ------------------

def instructions ():
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
        response = input(question).lower()

        if response == "yes" or response == "y":
            # if they say yes, return yes
            response = "yes"
            return response

        elif response == "no" or response == "n":
            # if no, then return no
            response = "no"
            return response

        else:
            print("please enter yes or no.")

# main routine goes here

show_instructions_q = "Have you played this game before? "
response = yes_no(show_instructions_q)
if response == "yes":
    print("program continues")
else:
    instructions()
