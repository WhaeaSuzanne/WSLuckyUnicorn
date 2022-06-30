"""
yes_no component
v1 - set up
v2 - set up quit code
v3 - turn into a function, which is much more efficient

"""
# functions go below this line ------------------
def yes_no(question):
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
    print("instructions")








