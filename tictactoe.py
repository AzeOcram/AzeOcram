import time
import random


grid_guide = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
]

grid = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
]

def show_board(grid):
    for rows in grid:
        print("[ " + "  ".join(rows) + " ]")
    time.sleep(0.5)

def show_guide(grid_guide):
    for rows in grid_guide:
        print(rows)

def player_play(grid):
    while True:    
        try:
            move = int(input("What's your move? [1-9]: ")) #check move if valid
            if move <= 9 and move > 0: #if valid
                print(f"Your move is {move}")
                time.sleep(0.5)

                #check validity of move
                if check_repetition(grid, move) == False:
                    place_move(move, "O") #if valid, then place move
                    break
                else:
                    print("Invalid move, that cell is already taken") #if not valid print
                    continue
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Choice")

    show_board(grid) #show board

    #check for winner
    win = check_winner(grid)
    if win:
        print("You win!")
        time.sleep(2)
        #play again
        play_again(grid)
    elif check_tie(grid):  # Check for tie
        print("It's a tie!")
        time.sleep(2)
        play_again(grid)
    else:
        bot_play(grid)

def bot_play(grid):
    print("Bot is playing...")
    time.sleep(1)
    while True:
        move = random.randrange(1, 9)
        if check_repetition(grid, move) == False:
            place_move(move, "X") #if valid, then place move
            break
        else:
            continue

    #show_board
    show_board(grid)
    
    #check for win
    win = check_winner(grid)
    if win:
        print("You lose!")
        time.sleep(2)
        #play again
        play_again(grid)

    elif check_tie(grid):  # Check for tie
        print("It's a tie!")
        time.sleep(2)
        play_again(grid)
    else:
        player_play(grid)

def place_move(move, x):
    if move <= 3:
            grid[0][move - 1] = x
    elif move <= 6:
        grid[1][move - 4] = x
    else:
        grid[2][move - 7] = x

def check_winner(grid):
    #for rows
    for row in grid:
        if (row[0] == "X" and row[1] == "X" and row[2] == "X") or (row[0] == "O" and row[1] == "O" and row[2] == "O"):
            return True
    # for columns
    column1 = [grid[0][0], grid[1][0], grid[2][0]]
    column2 = [grid[0][1], grid[1][1], grid[2][1]]
    column3 = [grid[0][2], grid[1][2], grid[2][2]]

    if (column1 == ["X","X","X"] or column2 == ["X","X","X"] or column3 == ["X","X","X"]) or (column1 == ["O","O","O"] or column2 == ["O","O","O"] or column3 == ["O","O","O"]):
        return True
    
    #for diagonals
    diagonal1 = [grid[0][0], grid[1][1], grid[2][2]]
    diagonal2 = [grid[0][2], grid[1][1], grid[2][0]]

    if (diagonal1 == ["X","X","X"] or diagonal2 == ["X","X","X"]) or (diagonal1 == ["O","O","O"] or diagonal2 == ["O","O","O"]):
        return True
    
    return False

def check_tie(grid):
    for row in grid:
        if "_" in row:
            return False
    return True

def check_repetition(grid, move):
    cell = ""
    if move <= 3:
        cell = grid[0][move - 1]
    elif move <= 6:
        cell = grid[1][move - 4]
    else:
        cell = grid[2][move - 7]

    if cell == "X" or cell == "O":
        return True
    else:
        return False

def play_again(grid):
    while True:
        again = input("Do you want to play again? [y/n]: ")
        if again == "y":
            print("Playing again...")
            time.sleep(0.5)

            #reset grid
            grid[:] = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]]

            print("Board has been reset")
            time.sleep(0.5)
            main_game(grid)
        if again == "n":
            print("Thanks for playing!")
            return
        else:
            print("Invalid choice")

def main_game(grid):
    while True:
        first = input("Do you want to play first? [y/n]: ")
        if first == "y":
            player_play(grid)
            break
        elif first == "n":
            bot_play(grid)
            break
        else:
            print("Invalid choice")


#Main Code
print("Let's play Tic-Tac-Toe!!")
time.sleep(1)

#Show board
print("Here is the board")
show_board(grid)
time.sleep(1)

#Show guide
print("Here is your guide")
show_guide(grid_guide)
time.sleep(1)


#Ready to play
count = 0
while True:
    ready = input("Are you ready to play? [y/n]: ")
    if ready == "y":
        main_game(grid)
        break
    if ready == "n":
        if count >= 1:
            exit = input("Do you want to exit [y/n]: ")
            if exit == "y":
                print("Thanks for playing!")
                break
        else:
            count += 1
            print("Okay let me know when you're ready!")
            time.sleep(2)


