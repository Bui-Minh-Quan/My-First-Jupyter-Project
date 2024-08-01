import curses
import time
from curses import wrapper

def start_screen(stdscr):
    stdscr.addstr("Welcome to Speed Typing Test!", curses.color_pair(3))
    stdscr.addstr(1, 0, "Press any key to begin!", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm = 0, accuracy_rate = 0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"{wpm} words per minute | Accuracy rate: {accuracy_rate}%")

    for i, char in enumerate(current):
        if char == target[i]:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        else:
            stdscr.addstr(0, i, target[i], curses.color_pair(2))

def correct_words_calculate(target_text, user_text):
    if len(target_text) == 0:
        return 0
    diff_check = False
    number_of_correct_words = 0
    for i in range(len(user_text)):
        if target_text[i] == " " or i == len(user_text) - 1: # reach a space or end of the line
            if diff_check == False:
                number_of_correct_words += 1
            diff_check = False
            continue
        if target_text[i] != user_text[i]:
            diff_check = True
    return number_of_correct_words
        

def wpm_test(stdscr):
    running = True
    wpm = 0
    start_time = time.time()
    total_words = 0
    correct_words = 0
    accuracy_rate = 0
    with open("typing_test_story.txt", "r") as file:
        while running:
            words_in_line = 0
            target_text = file.readline().strip()
            current_text = []
            if not target_text:
                    break #end of the file reached
            space_positions = []
            for i, char in enumerate(target_text):
                if char == " ":
                    space_positions.append(i)
            while True:
                try:
                    words_in_line = space_positions.index(len(current_text)) + 1
                except:
                    pass
                time_elapsed = max(time.time() - start_time, 1)
                wpm = round((total_words + words_in_line) / (time_elapsed / 60)) 
                stdscr.clear()
                if len(current_text) >= len(target_text):
                    words_in_line += 1
                    total_words += words_in_line
                    break
                display_text(stdscr, target_text, current_text, wpm, accuracy_rate)

                stdscr.refresh()

                key = stdscr.getkey()
                # Esc key pressed
                if key == "\x1b":
                    running = False
                    break
                if key in ('\x7f', '\b', curses.KEY_BACKSPACE):
                    if len(current_text) > 0:
                        current_text.pop()
                else:
                    current_text.append(key)
            
            current_text = "".join(current_text)
            correct_words += correct_words_calculate(target_text, current_text)
            if (total_words == 0):
                accuracy_rate = 0
            else: 
                accuracy_rate = round((correct_words / total_words) * 100) 
            



    

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.clear()

    start_screen(stdscr)
    wpm_test(stdscr)
    

wrapper(main)
