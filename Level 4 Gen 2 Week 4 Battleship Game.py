#game of Battleship:

ships = [
    [0, 1, 1, 0], # We put "1" to indicate there is a ship.
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0]
]

# Keep track of how many hits the player has and how many turns they have played in these variables
hits = 0
numberOfTurns = 0

# Allow the player to keep going until they have hit all four ships
while hits < 4:
    # Ask the player for a row
    row = int(input("Choose a row number between 0 and 3: "))
    # Ask the player for a column
    column = int(input("Choose a column number between 0 and 3: "))

    # Check if a ship exists in those coordinates
    if ships[row][column]:
        ships[row][column] = 0 # If the player hit a ship, remove it by setting the value to zero.
        hits += 1 # Increase the hit counter
        # Tell the player that they have hit a ship and how many ships are left
        print("Hit! {} left.\n".format(4-hits))
    else:
        print("Miss\n") # Tell the player that they missed

    numberOfTurns += 1 # Count how many turns the player has taken

print("Victory!")
print("You win in {} turns.".format(numberOfTurns))