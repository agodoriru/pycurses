import sys, os
import curses

show_list = '''show list'''

command_list = \
    '''
    help
    exit
    '''

show_help = \
    '''
    show help
    '''


def command_1(stdscr, y):
    if y == 4:
        stdscr.addstr(y, 1, "command 1", curses.color_pair(3))
    else:
        stdscr.addstr(4, 1, "command 1")


def command_2(stdscr, y):
    if y == 5:
        stdscr.addstr(y, 1, "command 2", curses.color_pair(3))
    else:
        stdscr.addstr(5, 1, "command 2")


def draw_menu(stdscr):
    user_input = 0
    cursor_x = 0
    cursor_y = 3

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # color
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:

        if user_input == ord('q'):
            sys.exit()

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if height < 20 and width < 80:
            sys.exit()

        if user_input == curses.KEY_DOWN:
            cursor_y += 1
        elif user_input == curses.KEY_UP:
            cursor_y -= 1
        elif user_input == curses.KEY_RIGHT:
            cursor_x += 1
        elif user_input == curses.KEY_LEFT:
            cursor_x -= 1

        # for vim key bind
        elif user_input == ord('j'):
            cursor_y += 1
        elif user_input == ord('k'):
            cursor_y -= 1
        elif user_input == ord('l'):
            cursor_x += 1
        elif user_input == ord('h'):
            cursor_x -= 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width - 1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height - 1, cursor_y)

        # Declaration of strings & Centering calculations
        main_pain = "main"[:width - 1]
        start_x_main_pain = int((width // 2) - (len(main_pain) // 2) - len(main_pain) % 2)
        start_y_main_pain = int(((height // 3) * 2) - 2)

        start_x_list = int((width // 2) - (len(show_list) // 2) - len(show_list) % 2)
        start_y_list = int((height // 6) - 2)

        v_line = "-" * (width - 2)

        # text for debug use
        window_status = "Window size Width: {}, Height: {}".format(width, height)
        cursor_status = "Cursor Position {} {}".format(cursor_x, cursor_y)
        status_bar = "STATUS BAR"

        if user_input == 0:
            user_input = "yet"
        key_status = "key : {}".format(user_input)

        stdscr.addstr(0, 0, window_status, curses.color_pair(1))
        stdscr.addstr(1, 0, cursor_status)
        stdscr.addstr(2, 0, key_status)

        stdscr.addstr(height - 1, 0, status_bar, curses.color_pair(3))
        stdscr.addstr(10, 1, v_line, curses.color_pair(4))
        stdscr.addstr(5, 1, command_list)

        command_1(stdscr, cursor_y)
        command_2(stdscr, cursor_y)

        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(start_y_main_pain, start_x_main_pain, main_pain, curses.color_pair(1))
        stdscr.addstr(start_y_list, start_x_list, show_list, curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        stdscr.move(cursor_y, cursor_x)

        stdscr.refresh()

        user_input = stdscr.getch()


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
