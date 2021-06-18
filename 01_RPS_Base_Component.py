import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")


        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
            else:
                print(error)

            print()

# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user # of rounds then loop...
rounds_played = 0


# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Rounds {} of {}".format(rounds_played + 1, rounds)

    print(heading)

    rounds_played +=1

    # Ask user for choice and check it's valid
    choose_error = "Please enter rock / paper / scissors (r / p / s) or xxx to quit"
    choose = choice_checker(choose_error, rps_list,
                            choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Computer Chose", comp_choice)

    # compare choice


    #end game if exit code is typed
    if choose == "xxx":
        break

    #  ***** rest of loop / game *****
    print("You chose {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played


# end of game
print("Thank you for playing")