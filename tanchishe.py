import curses
import random

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)

w.keypad(1)
w.timeout(100)

snk_x = sw//4
snk_y = sh//2
snk_body = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake_hits_wall(snk_body, snk_x, snk_y, sw, sh) or snake_hits_self(snk_body):
        curses.endwin()
        quit()

    new_head = [snk_y, snk_x]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snk_body.insert(0, new_head)

    if snk_body[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snk_body else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snk_body.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snk_body[0][0], snk_body[0][1], curses.ACS_CKBOARD)

def snake_hits_wall(snk_body, head_x, head_y, sw, sh):
    return head_x == 0 or head_x == sw-1 or head_y == 0 or head_y == sh-1

def snake_hits_self(snk_body):
    return snk_body[0] in snk_body[1:]

curses.endwin()
