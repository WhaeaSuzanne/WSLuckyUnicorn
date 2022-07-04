# trialing the token generator
# v1
# v2 - set the balance and format the print statments
import random

# set tokens so that unicorn is less likely to be chosen
tokens = ["unicorn", "horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

# testing loop to generate 20 tokens
x = 0
for item in range(0, 100):
    chosen = random.choice(tokens)
    # x += 1
    # print(x, chosen, end='\t')

    # adjust the balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5
print()
print("Starting balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))


