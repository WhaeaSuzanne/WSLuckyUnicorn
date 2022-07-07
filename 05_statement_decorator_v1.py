# create a decorated statement function

def statement_generator (statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# main routine
welcome_greeting = "Welcome to the Lucky Unicorn game."
welcome_decoration = "*"

statement_generator(welcome_greeting, welcome_decoration)
print()
unicorn_statement = "Congratulations, you got a unicorn"
unicorn_decoration = "!"
statement_generator(unicorn_statement,unicorn_decoration)
