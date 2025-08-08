import curses
import time

# Object Symbols
PLAYER = '🦧'
BARREL = 'O'
GROUND = '-'
EMPTY = ' '

# Game Screen Size
GAME_HEIGHT = 20
GAME_WIDTH = 40

# Jump
JUMP_HEIGHT = 4
JUMP_DELAY = 0.05

#Platform Height
platform_y = GAME_HEIGHT - 2 # 바닥 y좌표 (아래에서 2번째 줄)
stdscr = curses.initscr()

def draw_game(stdscr, player_x, player_y, barrels, lives):
    stdscr.clear() # Screen Init

    # platform
    for x in range(GAME_WIDTH):
        stdscr.addch(platform_y, x, GROUND)

    # barrel
    for barrel in barrels:
        try:
            stdscr.addch(barrel['y'], barrel['x'], BARREL)
        except curses.error:
            pass

    # player position
    try:
        stdscr.addstr(player_y, player_x, PLAYER)
    except curses.error:
        pass

    stdscr.addstr(0, 25, "Exit : press ESC")
    stdscr.refresh()

    # lifes
    stdscr.addstr(0, 2, f"Lives: {lives}")
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    # init player
    player_x = 5
    player_y = platform_y - 1

    # init jump
    is_jumping = False
    jump_counter = 0

    # init barrel
    barrels = [{'x': 30, 'y': platform_y - 1, 'dir': -1}]
    lives = 3
    game_over = False

    # Main Loop
    while not game_over:
        
        key = stdscr.getch()

        if key == 27:
            break

        # move
        if key == curses.KEY_LEFT and player_x > 0:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < GAME_WIDTH - 2:
            player_x += 1
        # start jump
        elif key == curses.KEY_UP and not is_jumping and player_y == platform_y - 1:
            is_jumping = True
            jump_counter = JUMP_HEIGHT

        # jumping
        if is_jumping:
            if jump_counter > 0:
                player_y -= 1
                jump_counter -= 1
            else:
                is_jumping = False

        # gravity
        elif player_y < platform_y - 1:
            player_y += 1 # 아래로 1 이동

        # barrel movement
        for barrel in barrels:
            barrel['x'] += barrel['dir']
            
            if barrel['x'] <= 0 or barrel['x'] >= GAME_WIDTH - 1:
                barrel['dir'] *= -1

            # collision
            if barrel['x'] == player_x and barrel['y'] == player_y:
                lives -= 1
                
                player_x = 5
                is_jumping = False
                jump_counter = 0
                time.sleep(0.5)
                if lives <= 0:
                    game_over = True

        draw_game(stdscr, player_x, player_y, barrels, lives)
        time.sleep(JUMP_DELAY)

    # game over message
    stdscr.nodelay(False)
    stdscr.clear()
    if lives <= 0:
            stdscr.addstr(GAME_HEIGHT // 2, GAME_WIDTH // 2 - 5, "💀 Game Over! 💀")
    else:
            stdscr.addstr(GAME_HEIGHT // 2, GAME_WIDTH // 2 - 5, "👋 Good Bye!")
    stdscr.refresh()
    stdscr.getch()

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nGame exited by user. Goodbye!")