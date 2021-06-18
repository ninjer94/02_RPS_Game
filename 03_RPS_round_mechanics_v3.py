# Main routine more efficient than v2


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an " \
                      "integer that is more than 0\n"

        # If infinity mode not chosen, check response
        # is an integer that is more than 0
        if response !="":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue
                else:
                    return response

            except ValueError:
                print("oops")



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
                                return response

                                # output error if item not in list
                            print(error)
                            print()

# Main routine goes here...

rounds_played = 0
choose_instruction = "please choose rock (r), paper (p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    #Rounds heading
    print()

    heading = "Round {} of " \
              "{}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to "
                   "end: ".format(choose_instruction))

    # End game if exit code is typed
    if choose == "xxx":
        break

    #  ***** rest of loop / game *****
    print("You choose {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Put end game content here
print("Thank you for playing")
