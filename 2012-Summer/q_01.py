# Answer to Programming 2012-Summer exam

_board_w = 9
_board_h = 15

def convert_display_board(value=0, method=0):
    if method == 0:
        if value == 0:
            return " "
        if value == 1:
            return "|"
        if value == 2:
            return "."
        if value == 3:
            return "-"
        if value == 4:
            return "V"
        if value == 5:
            return "O"
        if value == 6:
            return "X"
        if value == 7:
            return "e"
        else:
            return "?"


def render_board(board, method=0):
    # display board
    if method == 0:
        for i in range(len(board)):
            print(convert_display_board(board[i], method), sep='', end='')
            if i % _board_w == _board_w - 1:
                print() # new line
        return
    if method == 1:
        pass
    if method == 3:
        pass


def init_board(board, V_pos=4, X_pos=4):
    for i in range(len(board)):
        if i < _board_w:
            board[i] = 3
        if i >= (_board_h - 1) * _board_w and i < _board_h * _board_w:
            board[i] = 2
        if i % _board_w == 0 or i % _board_w == _board_w - 1:
            board[i] = 1
        if i == V_pos:
            board[i] = 4
        if i == (_board_h - 1) * _board_w + X_pos:
            board[i] = 6


def main():
    b = [0 for i in range(_board_w*_board_h)]
    init_board(b)
    render_board(b)


if __name__ == "__main__":
    main()
