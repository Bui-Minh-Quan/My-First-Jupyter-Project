import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.addstr("Welcome to Speed Typing Test!", curses.color_pair(3))
    stdscr.addstr("Press any key to begin!", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()


def wpm_test(stdscr):
    target_text = "Hello world. This is some test text for this app!"
    current_text = []
    
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.clear()

    start_screen(stdscr)
    wpm_test(stdscr)
    

wrapper(main)
