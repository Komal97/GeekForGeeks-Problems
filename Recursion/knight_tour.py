'''
https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
The knight is placed on the first block of an empty board and, moving according to the rules of chess, must visit each square exactly once.
Display all configuration.
'''

def displayBoard(chess):
    
    for i in range(len(chess)):
        for j in range(len(chess)):
            print(chess[i][j], end = ' ')
        print()
    print()

def printKNightBoard(chess, r, c, move):
    
    # if row or column goes out of board or cell is already occupied 
    if r < 0 or c < 0 or r >= len(chess) or c >= len(chess) or chess[r][c] > 0:
        return 

    # place last move and display board
    elif move == len(chess)*len(chess):
        chess[r][c] = move
        displayBoard(chess)
        chess[r][c] = 0
        return
    
    # enter move number at current position
    chess[r][c] = move    
    
    # move in all 8 directions
    printKNightBoard(chess, r-2, c+1, move+1)
    printKNightBoard(chess, r-1, c+2, move+1)
    printKNightBoard(chess, r+1, c+2, move+1)
    printKNightBoard(chess, r+2, c+1, move+1)
    printKNightBoard(chess, r+2, c-1, move+1)
    printKNightBoard(chess, r+1, c-2, move+1)
    printKNightBoard(chess, r-1, c-2, move+1)
    printKNightBoard(chess, r-2, c-1, move+1)
    
    # while returning, reset move so that other configuration can be find out
    chess[r][c] = 0


if __name__ == '__main__':
    n = int(input())                        # chess size
    r = int(input())                        # row of first move
    c = int(input())                        # col of first move
    chess = [[0 for _ in range(n)] for _ in range(n)]
    printKNightBoard(chess, r, c, 1)