def print_sudoku(string_representation):
    """
    prints a sudoku in a more readable format
    """
    for row in range(0, 81, 9):
        if row%27 == 0:
            print(29*"-")
        for col in range(0,9):
            if col%3 == 0:
                print("|", end="")
            print(string_representation[row+col], end="  ")
        print("\n")

example = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8"
print_sudoku(example)
"""test"""