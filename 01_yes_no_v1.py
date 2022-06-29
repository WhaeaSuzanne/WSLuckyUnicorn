# ask user if they have played before
show_instructions = input("Have you played this game before? ").lower()

#if they say yes, output "program continues"
if show_instructions == "yes" or show_instructions == "y":
    print("program continues")

#if no, then display "instructions"
elif show_instructions == "no" or show_instructions == "n":
    print("instructions")

else:
    print("please enter yes or no.")

    





