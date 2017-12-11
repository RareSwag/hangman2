# Hangman, Jaden H.
import random
import os
path = "puzzles"

def start_screen():
    print("")
    file = "art/start.txt"
    with open(file, "r") as f:
        lines = f.read()
    print(lines[12:])

def end_screen():
    print("")
    file = "art/ends.txt"
    with open(file, "r") as f:
        lines = f.read()
    print(lines)

def get_puzzle():
    path = "puzzles"
    fun_file = ""
    file_names = os.listdir(path)
    for i, f in enumerate(fun_file):
        print(str(i + 1) + "/" + f)
    print()

    choice = input("Pick One Fam  ")
    choice = int(choice) - 1

    file = path + "/" + file_names[choice]

    with open(file, "r") as f:
        lines = f.read().splitlines()
        
    puzzle = random.choice(lines[1:])
        
    return random.choice( lines[1:] )

def get_solved(puzzle, guesses):
    solved = ""
    for letter in puzzle:
        if letter.lower() in guesses.lower():
            solved += letter
        else:
            solved += "-"
    return (solved)


def check_strikes(puzzle, guesses, strikes):
        if guesses[-1] in puzzle:
            return strikes
        strikes += 1
        return strikes
            
def get_guess():
    print()
    letter = input("Gimme a letter that might be in the word thank! ")
    print()
    if len(letter) <= 1:
        return str(letter)
    else:
        print("You can only type in 1 letter fam!")
        return get_guess()
            
def display_board(solved, guesses, strikes):
    for i in range(strikes):
            print("")
            file = "art/apple.txt"
            with open(file, "r") as f:
                lines = f.read()
            print(lines[13:])
    print()
    print(solved + "        (" + guesses + ")")


def show_result(strikes, limit, puzzle):
    if strikes == limit:
        print("You lost and the word was " + puzzle + ".")
    else:
        print("You got it in " + str(limit - strikes) + " guesses. GJ.")
        

def play():
    strikes = 0
    limit = 7
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses, strikes)

    while solved != puzzle and strikes != limit:
        if strikes != limit:
            print("You have " + str(limit - strikes) + " guesses left")
            print()
            guesses += get_guess()
            solved = get_solved(puzzle, guesses)
            strikes = check_strikes(puzzle, guesses, strikes)
            display_board(solved, guesses, strikes)
        else:
            print("You ran out of guesses fam wow.")
            print()

    show_result(strikes, limit, puzzle)

def play_again():
    print()
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.upper()
        print()
        if decision == 'Y' or decision == 'YES':
            return True
        elif decision == 'N' or decision == 'NO':
            return False
        else:
            print()
            print("I don't understand. Please enter 'y' or 'n'.")


start_screen()

playing = True
while playing == True:
    play()
    playing = play_again()

end_screen()
