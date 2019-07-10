#10/07/19
# V 1.10
# Ethan Basford

from pprint import pprint as pp
import random
x = 0
Rows = 0
Columns = 0
turns = 0

print("Welcome to battleship!")

while (Rows > 10) or (Columns > 10) or (Rows <= 0) or (Columns <= 0):
    Rows = int(input("Please enter the number of rows you want. \n"))
    Columns = int(input("Please enter the number of columns you want. \n"))

def create_grid(Rows, Columns):
    #Creates the 2D Data Grid for computer
    grid1 = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
            row.append(' ')
        grid1.append(row)
    return grid1

grid1 = create_grid(Rows,Columns)

def display_grid(grid1, Columns):
    #Prints the labels for the grid
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
    print('  | ' + ' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid1):
       print(number + 1, '| ' + ' | '.join(row) + ' |')

grid1 = create_grid(Rows, Columns)
display_grid(grid1, Columns)
print ("Enemies grid") 






def random_row(grid1):
    #Makes a random row integer
    return random.randint(1,len(grid1))

def random_col(grid1):
    #Makes a random column integer
    return random.randint(1,len(grid1[0]))

def update_gridHit(grid1, GuessRow, GuessColumn):
    grid1[GuessRow-1][GuessColumn-1] = 'O'

def update_gridMiss(grid1, GuessRow, GuessColumn):
    grid1[GuessRow-1][GuessColumn-1] = 'X'




ShipRow = random_row(grid1)
ShipColumn = random_col(grid1)






def create_grid(Rows, Columns):
    #Creates the 2D Data Grid
    grid = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
            row.append(' ')
        grid.append(row)
    return grid

grid = create_grid(Rows,Columns)

def display_grid(grid, Columns):
    #Prints the labels for the grid
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
    print('  | ' + ' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid):
       print(number + 1, '| ' + ' | '.join(row) + ' |')

grid = create_grid(Rows, Columns)
display_grid(grid, Columns)

print ("Your grid") 






while x == 0:
    GuessRow = int(input("What row do you guess? \n"))
    GuessColumn = int(input("What column do you guess? \n"))

    if (GuessRow == ShipRow) and (GuessColumn == ShipColumn):
        turns += 1
        update_gridHit(grid1, GuessRow, GuessColumn)
        display_grid(grid1, Columns)
        print("You hit the battleship! Congratulations!")
        break

    elif (GuessRow < 1 or GuessRow > Rows) or (GuessColumn < 1 or GuessColumn > Columns):
        #Warning if the guess is out of the board
        print("Outside the set grid. Please pick a number within it your Rows and Columns.")

    elif (grid1[GuessRow-1][GuessColumn-1] == "X"):
        #If "X" is there than print that it missed
        print("You guessed that already.")

    else:
        #Updates the grid with an "X" saying that you missed the ship
        turns += 1
        print("You missed the ship.")
        update_gridMiss(grid1, GuessRow, GuessColumn)
        display_grid(grid1, Columns)









    c_row = random.randint(1,len(grid))
    c_column = random.randint(1,len(grid))

    if (c_row == ShipRow) and (c_column == ShipColumn):
        turns += 1
        update_gridHit(grid, c_row,c_column)
        display_grid(grid, Columns)
        print("The computer hit the battleship! Unlucky!")
        break
 
        
    if (c_row < 1 or c_row > Rows) or (c_column < 1 or c_column > Columns):
        #Warning if the guess is out of the board
        print("Outside the set grid. Please pick a number within it your Rows and Columns.")

        
    else:
        #Updates the grid with an "X" saying that you missed the ship
        turns += 15
        print("The computer missed the ship.")
        update_gridMiss(grid,c_row, c_column)
        display_grid(grid, Columns)


    

    

        
