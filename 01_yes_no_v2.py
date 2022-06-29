"""
yes_no component
v1 - set up
v2 - set up quit code

"""
show_instructions = ""

while show_instructions != "xxx":
    # ask user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    #if they say yes, output "program continues"
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")
        break

    #if no, then display "instructions"
    elif show_instructions == "no" or show_instructions == "n":
        print("instructions")
        break
    else:
        print("please enter yes or no.")







