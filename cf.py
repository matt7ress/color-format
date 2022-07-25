import colorama
colorama.init()
def format(tof: str) -> str:
    text = ''
    case = 0
    for char in tof:
        if(char == '!'):
            if(case == 0):
                case = 1
            elif(case == 1):
                text += '!'
                case = 0
        else:
            if(case == 0):
                text += char
            else:
                if(case == 1):
                    if(char == 'c'):
                        case = 2
                    elif(char == 'b'):
                        case = 3
                    elif(char == 'e'):
                        case = 4
                elif(case == 2):
                    if(char == ':'):
                        case = 5
                    elif(char == '^'):
                        case = 6
                elif(case == 3):
                    if(char == ':'):
                        case = 7
                    elif(char == '^'):
                        case = 8
                elif(case == 4):
                    if(char == ':'):
                        case = 9
                elif(case == 5):
                    if(char == 'B'):
                        text += colorama.Fore.BLACK
                    elif(char == 'R'):
                        text += colorama.Fore.RED
                    elif(char == 'g'):
                        text += colorama.Fore.GREEN
                    elif(char == 'y'):
                        text += colorama.Fore.YELLOW
                    elif(char == 'b'):
                        text += colorama.Fore.BLUE
                    elif(char == 'm'):
                        text += colorama.Fore.MAGENTA
                    elif(char == 'c'):
                        text += colorama.Fore.CYAN
                    elif(char == 'w'):
                        text += colorama.Fore.WHITE
                    elif(char == 'r'):
                        text += colorama.Fore.RESET
                    case = 0
                elif(case == 6):
                    if(char == 'B'):
                        text += colorama.Fore.LIGHTBLACK_EX
                    elif(char == 'r'):
                        text += colorama.Fore.LIGHTRED_EX
                    elif(char == 'g'):
                        text += colorama.Fore.LIGHTGREEN_EX
                    elif(char == 'y'):
                        text += colorama.Fore.LIGHTYELLOW_EX
                    elif(char == 'b'):
                        text += colorama.Fore.LIGHTBLUE_EX
                    elif(char == 'm'):
                        text += colorama.Fore.LIGHTMAGENTA_EX
                    elif(char == 'c'):
                        text += colorama.Fore.LIGHTCYAN_EX
                    elif(char == 'w'):
                        text += colorama.Fore.LIGHTWHITE_EX
                    case = 0
                elif(case == 7):
                    if(char == 'B'):
                        text += colorama.Back.BLACK
                    elif(char == 'R'):
                        text += colorama.Back.RED
                    elif(char == 'g'):
                        text += colorama.Back.GREEN
                    elif(char == 'y'):
                        text += colorama.Back.YELLOW
                    elif(char == 'b'):
                        text += colorama.Back.BLUE
                    elif(char == 'm'):
                        text += colorama.Back.MAGENTA
                    elif(char == 'c'):
                        text += colorama.Back.CYAN
                    elif(char == 'w'):
                        text += colorama.Back.WHITE
                    elif(char == 'r'):
                        text += colorama.Back.RESET
                    case = 0
                elif(case == 8):
                    if(char == 'B'):
                        text += colorama.Back.LIGHTBLACK_EX
                    elif(char == 'r'):
                        text += colorama.Back.LIGHTRED_EX
                    elif(char == 'g'):
                        text += colorama.Back.LIGHTGREEN_EX
                    elif(char == 'y'):
                        text += colorama.Back.LIGHTYELLOW_EX
                    elif(char == 'b'):
                        text += colorama.Back.LIGHTBLUE_EX
                    elif(char == 'm'):
                        text += colorama.Back.LIGHTMAGENTA_EX
                    elif(char == 'c'):
                        text += colorama.Back.LIGHTCYAN_EX
                    elif(char == 'w'):
                        text += colorama.Back.LIGHTWHITE_EX
                    case = 0
                elif(case == 9):
                    char = char.lower()
                    if(char == 'b'):
                        text += colorama.Style.BRIGHT
                    elif(char == 'd'):
                        text += colorama.Style.DIM
                    elif(char == 'n'):
                        text += colorama.Style.NORMAL
                    elif(char == 'r'):
                        text += colorama.Style.RESET_ALL
                    elif(char == 'u'):
                        text += '\x1b[4m'
                    elif(char == 'i'):
                        text += '\x1b[7m'
                    case = 0
    return text