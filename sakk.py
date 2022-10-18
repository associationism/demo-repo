import random
import time

def main():   
    board = [['0' for x in range(8)] for y in range(8)]
    wk = rand_position()
    board[wk[0]][wk[1]] = 'W'
    occupied = set_bad_coords_for_king(wk)
    bk = wk
    while not is_good_pos(occupied, bk):
        bk = rand_position()
    board[bk[0]][bk[1]] = 'B'
    rook = wk
    while not is_good_for_rook(rook, wk, bk):
        rook = rand_position()
    board[rook[0]][rook[1]] = 'R'
    draw_board(board)

def set_bad_coords_for_king(pos):
    x_coords = [ pos[0], pos[0]-1, pos[0]+1 ]
    y_coords = [ pos[1], pos[1]-1, pos[1]+1 ]
    return (x_coords, y_coords)

def is_good_for_rook(rook,wk,bk):
    if rook == wk or rook == bk:
        return False
    return True

def is_good_pos(bad_coords, pos):
    x,y = pos
    if x in bad_coords[0] and y in bad_coords[1]:
        return False
    return True

def draw_board(board):
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    counter = 8
    print(f'   {abc}')
    for line in board:
        print(f'{counter}. {line}')
        counter -= 1
    print(f'   {abc}')
    
def rand_position():
    x = random.randint(0,7)
    time.sleep(0.1)
    y = random.randint(0,7)
    return (x,y)

if __name__ == "__main__":
    main()