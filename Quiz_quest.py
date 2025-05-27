import random


def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()


def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter a yes / no")


def instructions():
    print('''
To Begin the game choose the amount of questions
you wish to be asked, or press <enter> for
infinite mode.

Then choose the difficulty level you want.

your goal is to answer as many questions as you
can correctly.

press xxx end the game at anytime.
Good luck!

    ''')


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
        else:
                print("please enter a number between 1 and 4")




response = "regular"
mode = "regular"
level = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

correct = 0
incorrect = 0

game_history = []

print()
print("welcome to the quiz quest")
print()

want_instructions = yes_no("Do you want to see the instructions? ")
print(f"you chose {want_instructions}")

# Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()


num_rounds = int_check("How many questions? <enter for infinite>: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

levels_select = level_check("What level? ")

if levels_select == "Level 1":
    level = "level 1"
elif levels_select == "level 2":
    level = "level 2"
elif levels_select == "level 3":
    level = "level 3"
elif levels_select == "level 4":
    level = "level 4"

    #if user_choice == "xxx":   


while rounds_played < num_rounds:


    if mode == "infinite":
        rounds_heading = f"\n Questions {rounds_played + 1} (Infinite Mode) "

    else:
        rounds_heading = f"\n Questions {rounds_played + 1} of {num_rounds} "


    print(rounds_heading)

    guess = ""
    if guess == "xxx":
        end_game = "yes"
        break

    if level == "level 1":
        levels_select = 1
        num_1 = random.randint(1, 500)
        operator = random.randint(1, 500)
        ans = num_1 + operator
        question = f"{num_1} + {operator} ="
        print(question)
        user_choice = int_check("answer: ")
        if user_choice == ans:
            feedback = ("correct")
            correct += 1
        else:
            feedback = ("incorrect, "
                        f"the correct answer was {ans}")
            incorrect += 1
        print(feedback)
        if user_choice == "xxx":
            break


    elif level == "level 2":
        levels_select = 2
        num_1 = random.randint(1, 500)
        operator = random.randint(1, 500)
        ans = num_1 - operator
        print(f"{num_1} - {operator} =")

        user_choice = int_check("answer: ")
        if user_choice == ans:
            feedback = ("correct")
            correct += 1
        else:
            feedback = ("incorrect, "
                        f"the correct answer was {ans}")
            incorrect += 1
        print(feedback)
        if user_choice == "xxx":
            break


    elif level == "level 3":
        levels_select = 3
        num_1 = random.randint(1, 100)
        operator = random.randint(1, 10)
        ans = num_1 * operator
        print(f"{num_1} x {operator} =")

        user_choice = int_check("answer: ")
        if user_choice == ans:
            feedback = ("correct")
            correct += 1
        else:
            feedback = ("incorrect, "
                        f"the correct answer was {ans}")
            incorrect += 1
        print(feedback)
        if user_choice == "xxx":
            break



    elif level == "level 4":
        levels_select = 4
        num_1 = random.randint(1, 500)
        operator = random.randint(1, 10)
        ans = num_1 / operator
        print(f"{num_1} / {operator} =")

        user_choice = int_check("answer: ")
        if user_choice == ans:
            feedback = ("correct")
            correct += 1
        else:
            feedback = ("incorrect, "
                        f"the correct answer was {ans}")
            incorrect += 1
        print(feedback)
        if user_choice == "xxx":
            break


    rounds_played += 1

    history_feedback = f"Round {rounds_played}: {feedback}"
    history_item = f"round: {rounds_played} - {history_feedback}"

    print(history_feedback)
    game_history.append(history_item)

if rounds_played > 0:
    rounds_correct = rounds_played - incorrect
    percent_won = rounds_correct / rounds_played * 100
    percent_lost = incorrect / rounds_played * 100

    print( "game results ")
    print(f"Correct: {percent_won:.2f} \t "
          f"incorrect: {percent_lost:.2f}")

    see_history = string_checker("\nDo you want to see the game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing.")





#print(round_feedback)
    #game_history.append(history_item)

