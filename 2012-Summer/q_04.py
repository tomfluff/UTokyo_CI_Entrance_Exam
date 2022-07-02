# Answer to Programming 2012-Summer exam
import random

_board_w = 9
_board_h = 15
_max_bullets = 2

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
    target_source_loc = 4
    bullet_source_loc  = 4
    init_board(b, target_source_loc, bullet_source_loc)
    render_board(b)

    game_score = 0

    target_loc = 0
    target_x_dir = 1
    bullet_loc = [0 for i in range(_max_bullets)]
    bullet_counter = 0

    while True:
        c = input()
        if c == 'e':
            break
        if c not in ['i','j','k','l','']:
            continue

        if target_loc == 0:
            b[target_source_loc] = 3
            target_source_loc = random.randint(1, _board_w-2)
            b[target_source_loc] = 4
            target_x_dir = -1 if target_source_loc == _board_w-2 else 1
            target_loc = target_source_loc + _board_w + target_x_dir
        else:
            b[target_loc] = 0 if b[target_loc] == 5 else b[target_loc]
            new_target_loc = target_loc + _board_w + target_x_dir
            if b[new_target_loc] in [1]:
                target_x_dir *= -1
                new_target_loc = target_loc + _board_w + target_x_dir
            if b[new_target_loc] in [2,6]:
                new_target_loc = 0
                target_x_dir = 1
            target_loc = new_target_loc
        if target_loc != 0 :
            b[target_loc] = 5
        
        # update bullets
        for i in range(len(bullet_loc)):
            b[bullet_loc[i]] = 0 if b[bullet_loc[i]] == 7 else b[bullet_loc[i]]
        for i in range(len(bullet_loc)):
            if bullet_loc[i] == 0:
                continue
            new_bullet_loc = bullet_loc[i] - _board_w
            if new_bullet_loc < _board_w:
                bullet_loc[i] = 0
                bullet_counter -= 1
                continue
            if new_bullet_loc == target_loc:
                bullet_loc[i] = 0
                bullet_counter -= 1
                b[target_loc] = 0
                target_loc = 0
                game_score += 1
                continue
            bullet_loc[i] = new_bullet_loc
            b[bullet_loc[i]] = 7

        # create new bullets if needed
        if c == 'i' and bullet_counter < _max_bullets:
            for i in range(len(bullet_loc)):
                if bullet_loc[i] == 0:
                    j = i
            bullet_loc[j] = (_board_h - 2) * _board_w + bullet_source_loc
            b[bullet_loc[j]] = 7
            bullet_counter += 1
        
        print("target: %d, bullets: %s, counter: %d" % (target_loc, str(bullet_loc), bullet_counter))
        print("score: %d" % (game_score))
        
        render_board(b)


if __name__ == "__main__":
    main()
