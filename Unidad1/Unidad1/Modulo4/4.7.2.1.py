'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 2 de Octubre del 2024
4.7.2.1 PROYECTO: TIC-TAC-TOE

'''
from random import randrange

def DisplayBoard(board):
    print("+-------" * 3 + "+")
    for row in board:
        print("|       " * 3 + "|")
        print("|  " + "  |  ".join(str(cell) for cell in row) + "  |")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

def EnterMove(board):
    free_fields = MakeListOfFreeFields(board)
    move = int(input("Ingresa tu movimiento: "))
    while (move < 1 or move > 9 or not any(move == board[r][c] for r, c in free_fields)):
        move = int(input("Movimiento inválido. Ingresa un número válido: "))
    for r, c in free_fields:
        if board[r][c] == move:
            board[r][c] = 'O'
            break

def MakeListOfFreeFields(board):
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] != 'O' and board[r][c] != 'X':
                free_fields.append((r, c))
    return free_fields

def VictoryFor(board, sign):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # Fila superior
        [(1, 0), (1, 1), (1, 2)],  # Fila del medio
        [(2, 0), (2, 1), (2, 2)],  # Fila inferior
        [(0, 0), (1, 0), (2, 0)],  # Columna izquierda
        [(0, 1), (1, 1), (2, 1)],  # Columna central
        [(0, 2), (1, 2), (2, 2)],  # Columna derecha
        [(0, 0), (1, 1), (2, 2)],  # Diagonal principal
        [(0, 2), (1, 1), (2, 0)]   # Diagonal secundaria
    ]
    
    for condition in win_conditions:
        if all(board[r][c] == sign for r, c in condition):
            return True
    return False

def DrawMove(board):
    free_fields = MakeListOfFreeFields(board)
    if free_fields:
        r, c = free_fields[randrange(len(free_fields))]
        board[r][c] = 'X'

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

DisplayBoard(board)
while True:
    EnterMove(board)
    DisplayBoard(board)
    
    if VictoryFor(board, 'O'):
        print("¡Has ganado!")
        break
    elif not MakeListOfFreeFields(board):
        print("Empate.")
        break
    
    DrawMove(board)
    DisplayBoard(board)
    
    if VictoryFor(board, 'X'):
        print("La máquina ha ganado.")
        break
    elif not MakeListOfFreeFields(board):
        print("Empate.")
        break
