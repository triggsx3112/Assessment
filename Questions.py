def int_check(question):

    while True:
        error = "please enter an integer that is 1 or more."

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def level_check(question):
    while True:


        response = input(question).lower()


        if response == "1" or response == "level 1":
            return "Level 1"
        elif response == "2" or response == "level 2":
            return "level 2"
        elif response == "3" or response == "level 3":
            return "level 3"
        elif response == "4" or response == "level 4":
            return "level 4"
        elif response == "5" or response == "level 5":
            return "level 5"
        else:
                print("please enter a number between 1 and 5")


rounds_played = 0
mode = "regular"
level = "regular"

levels_select = level_check("What level? ")

if levels_select == "level 1":
    level = "level 1"
    levels_select = 1

num_rounds = int_check("Rounds <enter for infinite>: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5




while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (infinite mode) "

    else:
        rounds_heading = f"\n round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)

    if rounds_played = 1
        int(input("3+5"))








    rounds_played += 1
