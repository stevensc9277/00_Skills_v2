valid = False
while not valid:
    # get input
    error = "Please a number from one to ten. "
    # ask user for name
    name = input("What is your name? ")

    # ask user for two numbers
    try:
        num_1 = int(input("Pick a number from one to ten. "))
        if num_1 > 10:
            valid = False
            while not valid:
                num_1 = int(input("Please pick a number from one to ten. "))
    except ValueError:
        print(error)
        print("")

    try:
        num_2 = int(input("Pick another number from one to ten. "))
        valid = True
    except ValueError:
        print(error)
        # add two numbers together
    num_3 = num_1 + num_2
    # multiply two numbers together
    num_4 = num_1 * num_2
    # greet user and display math
    print("The numbers that you have chosen add up to {}".format(num_3))
    print("Your numbers also multiply to get {}".format(num_4))
