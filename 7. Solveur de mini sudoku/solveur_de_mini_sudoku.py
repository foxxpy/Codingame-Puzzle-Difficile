import sys
import math

sudoku = []

def n_valide(i, j, n):
    global sudoku

    #On détermine si le nombre n'est pas déjà dans une ligne
    if n in sudoku[i]:
        return False

    #On détermine si le nombre n'est pas déjà dans une colonne
    for row in range(4):
        if sudoku[row][j] == n:
            return False

    row = (i//2) * 2
    col = (j//2) * 2

    #On détermine si le nombre est valide dans sa sous-grille 3x3
    for i in range(0,2):
        for j in range(0,2):
            if sudoku[row+i][col+j] == n:
                return False

    return True

def solve():
    global sudoku

    for i in range(4):
        for j in range(4):
            if sudoku[i][j] == "0":
                for n in range(1,5):
                    if n_valide(i, j, str(n)):
                        sudoku[i][j] = str(n)
                        print(sudoku, file=sys.stderr)
                        solve()
                        sudoku[i][j] = "0"
                return

    #On affiche la grille de sudoku
    for line in sudoku:
        print("".join(line))




#Instanciation des variables
line_1 = list(input())
line_2 = list(input())
line_3 = list(input())
line_4 = list(input())
sudoku = [line_1, line_2, line_3, line_4]

solve()