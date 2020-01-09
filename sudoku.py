board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(board):

    # Get location of blank space (0):
    find  = find_empty(board)

    if not find: # Base case, find_empty() returns None
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(board, i, (row, col)): 
            board[row][col] = i # Set if number is valid

            if solve(board): # Recursively call solve() until done
                return True
            
            board[row][col] = 0 # Set value to 0 and backtrack is False
    
    return False

def valid(board, num, pos):
    
    # Check Row:
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check Column:
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 Cube:
    box_x = pos[1] // 3 # Horizontal box : (left) 0 > 1 > 2 (right)
    box_y = pos[0] // 3 # Vertical box : (bottom) 2 ^ 1 ^ 0 (top)

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3): 
            if board[i][j] == num and (i, j) != pos:
                return False
    
    # Valid position:
    return True

def print_board(board):

    for i in range(len(board)):
        # Print horizontal separating line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")

        for j in range(len(board[0])):
            # Print vertical separating line
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            
            # Print the numbers
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end='')

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # Row, Col
    return None

# Main driver
print()
print('Original board:')
print()
print_board(board)
print()
solve(board)
print('Solved board:')
print()
print_board(board)
print()
