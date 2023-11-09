import random

line_1 = [" ", " ", " "]
line_2 = [" ", " ", " "]
line_3 = [" ", " ", " "]

game_end = False


def display():
    print(" %c | %c | %c " % (line_1[0], line_1[1], line_1[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (line_2[0], line_2[1], line_2[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (line_3[0], line_3[1], line_3[2]))
    print("   |   | ")


def replace():
    if choice == 1 and line_1[0] == " ":
        line_1[0] = "X"
    elif choice == 2 and line_1[1] == " ":
        line_1[1] = "X"
    elif choice == 3 and line_1[2] == " ":
        line_1[2] = "X"
    elif choice == 4 and line_2[0] == " ":
        line_2[0] = "X"
    elif choice == 5 and line_2[1] == " ":
        line_2[1] = "X"
    elif choice == 6 and line_2[2] == " ":
        line_2[2] = "X"
    elif choice == 7 and line_3[0] == " ":
        line_3[0] = "X"
    elif choice == 8 and line_3[1] == " ":
        line_3[1] = "X"
    elif choice == 9 and line_3[2] == " ":
        line_3[2] = "X"


def computer_choice():
    computer = random.randint(1, 9)
    if computer == 1 and line_1[0] == " ":
        line_1[0] = "O"
    elif computer == 2 and line_1[1] == " ":
        line_1[1] = "O"
    elif computer == 3 and line_1[2] == " ":
        line_1[2] = "O"
    elif computer == 4 and line_2[0] == " ":
        line_2[0] = "O"
    elif computer == 5 and line_2[1] == " ":
        line_2[1] = "O"
    elif computer == 6 and line_2[2] == " ":
        line_2[2] = "O"
    elif computer == 7 and line_3[0] == " ":
        line_3[0] = "O"
    elif computer == 8 and line_3[1] == " ":
        line_3[1] = "O"
    elif computer == 9 and line_3[2] == " ":
        line_3[2] = "O"
    else:
        computer_choice()


def check_results():
    global game_end
    game_end = True
    if line_1[0] == line_1[1] and line_1[1] == line_1[2] and line_1[2] != " ":
        if line_1[2] == "X":
            print("You Won!")
        elif line_1[1] == "O":
            print("Computer Won")
    elif line_2[0] == line_2[1] and line_2[1] == line_2[2] and line_2[2] != " ":
        if line_2[2] == "X":
            print("You Won!")
        elif line_2[1] == "O":
            print("Computer Won")
    elif line_3[0] == line_3[1] and line_3[1] == line_3[2] and line_3[2] != " ":
        if line_3[2] == "X":
            print("You Won!")
        elif line_3[1] == "O":
            print("Computer Won")
    elif line_1[0] == line_2[0] and line_2[0] == line_3[0] and line_2[0] != " ":
        if line_3[0] == "X":
            print("You Won!")
        elif line_2[0] == "O":
            print("Computer Won")
    elif line_1[1] == line_2[1] and line_2[1] == line_3[1] and line_3[1] != " ":
        if line_3[1] == "X":
            print("You Won!")
        elif line_2[1] == "O":
            print("Computer Won")
    elif line_1[2] == line_2[2] and line_2[2] == line_3[2] and line_3[2] != " ":
        if line_3[2] == "X":
            print("You Won!")
        elif line_3[2] == "O":
            print("Computer Won")
    elif line_1[0] == line_2[1] and line_2[1] == line_3[2] and line_3[2] != " ":
        if line_3[2] == "X":
            print("You Won!")
        elif line_3[2] == "O":
            print("Computer Won")
    elif line_3[0] == line_2[1] and line_2[1] == line_1[2] and line_1[2] != " ":
        if line_1[2] == "X":
            print("You Won!")
        elif line_1[2] == "O":
            print("Computer Won")
    elif line_1[0] != " " and line_1[1] != " " and line_1[2] != " " and line_2[0] != " " and line_2[1] != " " and \
            line_2[2] != " " and line_3[0] != " " and line_3[1] != " " and line_3[2] != " ":
        print("It's a draw")
    else:
        game_end = False

print("Welcome to Mariya's Tic Tac Toe game.\nRules:Your symbol is X,plase your symbol on the board,the goal is to get 3 of her marks in a row (up, down, across, or diagonally).\nFirst player achive the goal is the winner.")
print("Chose where on the board you want to place your X,\n"
      " 1  2  3 \n "
      "4  5  6 \n "
      "7  8  9 \n ")
while not game_end:
    choice = int(input("Type number from 1 to 9\n"))
    if 10 <= choice <= 0:
        choice = int(input("Type number from 1 to 9\n"))
    replace()
    display()
    print("Computer chose:")
    computer_choice()
    display()
    check_results()
