import os


def clear_screen():
    # clear the screen. posix is os name in Linux/Mac
    if os.name == 'posix':
        os.system('clear')
    else:
        # clear screen for windows
        os.system('cls')
