# trialing the token generator
# v1
# v2 - set the balance and format the print statments
import random

STARTING_BALANCE = 100

balance = STARTING_BALANCE

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


