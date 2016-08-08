def verify(board, lastmove):
    player = board[lastmove]
    for i in range(3):
        

def main():
    lastmove = [2][2]
    board = [[x,_,x],[o,x,o],[o,o,x]]
    print verify(board, lastmove)

if __name__ == '__main__':
    main()