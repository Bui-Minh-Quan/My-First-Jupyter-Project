import curses
import random
import time
from curses import wrapper

def start_screen(stdscr):
    stdscr.addstr("Welcome to Speed Typing Test!", curses.color_pair(3))
    stdscr.addstr(1, 0, "Press any key to begin!", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()



def display_text(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0,f"{wpm} words per minute")

    for i, char in enumerate(current):
        if char == target[i]:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        else:
            stdscr.addstr(0, i, target[i], curses.color_pair(2))


def wpm_test(stdscr):
    running = True
    wpm = 0
    start_time = time.time()
    words = 0
    with open("typing_test_story.txt", "r") as file:
        while running:
            target_text = file.readline().strip()
            current_text = []
            while True:
                if not target_text:
                    break #end of the file reached

                if len(target_text) <= len(current_text) or target_text[len(current_text)] == " ":
                    words += 1
                time_elapsed = max(time.time() - start_time, 1)
                wpm = round(words / (time_elapsed / 60)) 
                stdscr.clear()
                if len(current_text) >= len(target_text):
                    break
                display_text(stdscr, target_text, current_text, wpm)

                stdscr.refresh()

                key = stdscr.getkey()
                # Esc key pressed
                if key == "\x1b":
                    running = False
                    break
                if key == '\x7f' or key == '\b':
                    if len(current_text) > 0:
                        current_text.pop()
                else:
                    current_text.append(key)



    

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.clear()

    start_screen(stdscr)
    wpm_test(stdscr)
    

wrapper(main)
